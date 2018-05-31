from flask import Flask, jsonify, request, Response
from xai import app
import json
import requests
import time
import uuid
import copy

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


with open('xai/SamplePage/places.json', encoding="utf8") as f:
    spots = json.load(f)
    spots = spots["datas"]

# endpoints
@app.route("/", methods=['GET'])
def indexAction():
	return jsonify({
		'Hi': 'Server side works fine'
	})

@app.route("/"+app.config['API_VERSION']+"/greeting", methods=['GET'])
def addSubscriber():
	return jsonify({
		'foo': 'bar'
	})

@app.route("/"+app.config['API_VERSION']+"/reverse_echo", methods=['GET'])
def reverse_echo():
	s = request.args.get('s')
	time.sleep(1)
	if s:
		return jsonify({
			'status': 'OK',
			'result': s[::-1]
		})
	else:
		return jsonify({
			'status': 'Error',
			'message': 'The argument s is required.'
		})


@app.route("/"+app.config['API_VERSION']+"/gspread", methods=['GET'])
def gs():
	docID = "1YKDcX-hd2iskDhvNYHDFlKQniVoQRMaKJjA8uQHc_48"
	googleUrl = "https://spreadsheets.google.com/feeds"
	gsheetDatas = {
		"resourceId":docID,
		"type": "googleSheet",
		"datas" : []
	}
	credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', googleUrl)
	gs = gspread.authorize(credentials)	
	gsheet = gs.open_by_key(docID)
	wsheet = gsheet.sheet1
	values = wsheet.get_all_records()
	for value in values:
		gsheetData = {}
		gsheetData['title'] = value['title']
		gsheetData['description'] = value['content']
		gsheetData['images'] = dealMultidata(value['photos'])
		gsheetData['tags'] = dealMultidata(value['tags'])
		gsheetData['location'] = dealLocation(value['location'])
		gsheetDatas['datas'].append(gsheetData)
	
	return jsonify(gsheetDatas)


def dealMultidata(val):
	result = []
	if val.strip() != '':						
			items = val.split(',')
			for item in items:
				result.append(item)
	return result

def dealLocation(val):
	result = {}
	val = val.strip().replace(' ','')
	items = val.split(',')
	result['lat'] = float(items[0])
	result['lng'] = float(items[1])
	return result	


@app.route("/"+app.config['API_VERSION']+"/displayGroups", methods=['GET'])
def filters():	
	return jsonify(exportDisplayGroup())	

@app.route("/"+app.config['API_VERSION']+"/spots", methods=['GET'])
def show_spots():
	return jsonify(spots)

@app.route("/"+app.config['API_VERSION']+"/places", methods=['POST'])
def postPlaces():				
	places = []
	filterIds = request.get_json()["filterIds"]
	for spot in spots:
		for filterId in filterIds:
			for displayGroup in spot['displayGroups']:				
				if (displayGroup['displayGroupId'] == filterId) or (displayGroup['subDisplayGroupId'] == filterId):
					tmp_spot = copy.deepcopy(spot)
					del tmp_spot['images']
					del tmp_spot['fields']
					del tmp_spot['description']
					places.append(tmp_spot)
					break	

	return jsonify(places)

@app.route("/"+app.config['API_VERSION']+"/place", methods=['GET'])
def place():
	id = request.args.get('id')
	for spot in spots:
		if spot['id'] == id:
			return jsonify(spot)	

	return 	


@app.route("/"+app.config['API_VERSION']+"/fakeplaces", methods=['GET'])
def fakeplaces():
	docID = "1YKDcX-hd2iskDhvNYHDFlKQniVoQRMaKJjA8uQHc_48"
	googleUrl = "https://spreadsheets.google.com/feeds"
	gsheetDatas = {
		"resourceId":docID,
		"type": "googleSheet",
		"datas" : []
	}
	credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', googleUrl)
	gs = gspread.authorize(credentials)	
	gsheet = gs.open_by_key(docID)
	wsheet = gsheet.sheet1
	values = wsheet.get_all_records()
	for value in values:
		gsheetData = {}
		gsheetData['id'] = str(uuid.uuid4())
		gsheetData['title'] = value['title']
		gsheetData['description'] = value['content']
		gsheetData['images'] = ["https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/09cb5968-a61a-42af-9fdc-06605047a286.png"]#dealMultidata(value['photos'])
		gsheetData['icon-url'] = ["https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/09cb5968-a61a-42af-9fdc-06605047a286.png"]
		gsheetData['fields'] = []
		#gsheetData['tags'] = dealMultidata(value['tags'])
		gsheetData['location'] = dealLocation(value['location'])
		gsheetData['path'] = None

		gsheetData['displayGroups'] = []
		groups = exportDisplayGroup()
		displayGroup = {}
		for group in groups:
			displayGroup["displayGroupId" ] = group["id"]

			for subgroup in group['subDisplayGroups']:
				displayGroup['subDisplayGroupId'] = subgroup['id']

				for tag in dealMultidata(value['tags']):
					if tag == subgroup['name']:
						#print(tag+"/"+subgroup['name'])
						gsheetData['displayGroups'].append(copy.deepcopy(displayGroup))


		gsheetDatas['datas'].append(gsheetData)

	
	return jsonify(gsheetDatas)		


def exportDisplayGroup():
	displayGroups = []

	#group 1
	displayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "1",
		"name" : "電台",
		"subDisplayGroups" : []
	}

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "12",
		"name" : "新聞"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "13",
		"name" : "經典搖滾"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "14",
		"name" : "鄉村音樂"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "15",
		"name" : "流行音樂"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "16",
		"name" : "原住民電台"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "17",
		"name" : "經典音樂"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "18",
		"name" : "旅遊資訊"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)
	displayGroups.append(displayGroup)

	#group 2
	displayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "2",
		"name" : "新聞",
		"subDisplayGroups" : []
	}

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "21",
		"name" : "Chetwynd"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "22",
		"name" : "Dawson Creek"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)
	displayGroups.append(displayGroup)

	#group 3
	displayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "3",
		"name" : "電台",
		"subDisplayGroups" : []
	}

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "31",
		"name" : "Chetwynd"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "32",
		"name" : "Dawson Creek"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "33",
		"name" : "Fort St. John"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "34",
		"name" : "Tumbler Ridge"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "35",
		"name" : "Whitehorse"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	subDisplayGroup = {
		"defaultActivate" : True,
		"icon": "https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png",
		"id": "36",
		"name" : "Chetwynd"
	}
	displayGroup["subDisplayGroups"].append(subDisplayGroup)

	displayGroups.append(displayGroup)
	return displayGroups