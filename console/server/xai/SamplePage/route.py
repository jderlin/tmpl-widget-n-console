from flask import Flask, jsonify, request, Response
from xai import app
from Fungogo import Fungogo
import json
import requests
import time
import logging
import pprint
import string
import copy

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
pp = pprint.PrettyPrinter(indent=4)

# define constants

WEB_API_SERVER = 'http://FungogoWebF2EApiLB-1348326226.ap-northeast-2.elb.amazonaws.com/v1.0'
FUNSTORE_ID = '6eafc79d-8005-4695-aa3a-84b25315e06b'
VENDOR_AUTHORIZE = 'e21a93fc-d10b-4ead-8be8-bce282f7c5ea'

GOOGLE_SHEET_ID = '14jf2ZFOLqSSq9GIrSbOZSBhslpQIVIUs-IGMkKvjll0'

NUM_MAX_PHOTOS = 9
BATCH_GOOGLE_UPDATE_WINDOW = 200

import json
with open('xai/SamplePage/places.json', encoding="utf8") as f:
    spots = json.load(f)
with open('xai/SamplePage/filters.json', encoding="utf8") as f:
    filter_data = json.load(f)    

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

@app.route("/"+app.config['API_VERSION']+"/displayGroups", methods=['GET'])
def filters():
	return jsonify(filter_data)	

@app.route("/"+app.config['API_VERSION']+"/places", methods=['POST'])
def postPlaces():				
	places = []
	filterIds = request.get_json()["filterIds"]
	for spot in spots:
		for filterId in filterIds:
			if (spot['displayGroups'][0]['displayGroupId'] == filterId) or (spot['displayGroups'][0]['subDisplayGroupId'] == filterId):
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
@app.route("/"+app.config['API_VERSION']+"/getFungogoSpot", methods=['GET'])
def getFungogoSpot():
	return jsonify(spots)	
@app.route("/"+app.config['API_VERSION']+"/search", methods=['GET'])
def search():
	places = []
	filterIds = request.args.getlist('filterIds[]')	
	for spot in spots:
		for filterId in filterIds:
			if (spot['displayGroups'][0]['displayGroupId'] == filterId) or (spot['displayGroups'][0]['subDisplayGroupId'] == filterId):
				places.append(spot)
				break	

	return jsonify(places)	

@app.route("/"+app.config['API_VERSION']+"/filter", methods=['GET'])
def filter():
	return jsonify(filter_data)	

@app.route("/"+app.config['API_VERSION']+"/currentUserInfo", methods=['GET'])
def currentUserInfo():
	currentUserInfo = {
		"registerDate":"2018/02/14",
		"userInfo" : {
			"account" : "test",
			"email" : "jder@xotours-ai.xyz",
			"gender" : "man"
		}
	}
	return jsonify(currentUserInfo)