from flask import Flask, jsonify, request, Response
from xai import app
import json
import requests
import time

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
	filters = [
		{
		'id': '9beb08c9-5069-4cfb-8ff9-ce8f5fbf4c07',
		'name': '餐廳',
		'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/android.png',
		'defaultActivate': False,
		'subDisplayGroups':[
				{
					'id': 'a3079e3b-10c6-4274-a3e1-b36406bc552e',
					'name': '中式',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/area-chart.png',
					'defaultActivate': False
				},
				{
					'id': '34d6cf27-de11-4504-a980-32d9dcccdfc2',
					'name': '美式',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/arrow-down.png',
					'defaultActivate': False
				},
				{
					'id': 'a1365f37-bcb4-4183-adf3-26a83209b806',
					'name': '日式',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/asl-interpreting.png',
					'defaultActivate': False
				}
			]
		},
		{
		'id': 'f07bdd19-c156-4ad7-a296-e7f1c967ba5a',
		'name': '鳥類',
		'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/battery-2.png',
		'defaultActivate': False,
		'subDisplayGroups':[
				{
					'id': '358e74bf-a2a7-40d5-8e4b-6e8a30f1459f',
					'name': '大型',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/header/header_s_funbox.svg',
					'defaultActivate': True
				},
				{
					'id': '4dc5e881-48da-4fcc-8d76-e039d02e5f8f',
					'name': '中型',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/header/header_s_notice.svg',
					'defaultActivate': True
				},
				{
					'id': 'edfdccbd-d273-4124-aa27-4cd8409dd41d',
					'name': '小型',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/header/header_s_setting.svg',
					'defaultActivate': False
				}
			]
		},
		{
		'id': '8c29988c-e5e3-4bb1-9f5e-b3f9b35410fd',
		'name': '類別一',
		'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/header/header_s_notice.svg',
		'defaultActivate': False,
		'subDisplayGroups':[
				{
					'id': 'eedb5172-2a14-48c0-983d-256422b0fe49',
					'name': 'A式',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/header/header_s_booking.svg',
					'defaultActivate': False
				},
				{
					'id': '7d36e9ad-f2b1-475b-a4dc-f938b4c61ef6',
					'name': 'B式',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/menu/mytrip.png',
					'defaultActivate': False
				},
				{
					'id': '22f443ea-1ece-469a-9633-9ed2bff3b0ff',
					'name': 'C式',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/menu/car.png',
					'defaultActivate': False
				}
			]
		},
		{
		'id': 'ccb81ab5-6f50-4d2b-ad62-e3c54018364a',
		'name': '類別二',
		'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/header/header_s_booking.svg',
		'defaultActivate': True,
		'subDisplayGroups':[
				{
					'id': 'a6ce1532-e4ce-4377-97ab-afedb1f415ee',
					'name': '類別二',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/header/header_s_booking.svg',
					'defaultActivate': True
				}
			]
		},
		{
		'id': 'a4d5b6c8-dc45-4763-8e54-8e0519444847',
		'name': '類別三',
		'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/menu/mytrip.png',
		'defaultActivate': False,
		'subDisplayGroups':[
				{
					'id': '6cec10b4-36db-43be-a759-d7ef7fe06f6d',
					'name': '類別三',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/menu/mytrip.png',
					'defaultActivate': False
				}
			]
		},
		{
		'id': '404d398f-7520-4460-be22-629c30899d1c',
		'name': '類別四',
		'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/menu/car.png',
		'defaultActivate': False,
		'subDisplayGroups':[
				{
					'id': 'd2bb47fe-e013-47bc-bc15-f3c032535991',
					'name': '類別四',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Home/Images/menu/car.png',
					'defaultActivate': False
				}
			]
		},
		{
		'id': '28bc0fe3-aa1c-4474-8258-6f29c430562b',
		'name': '類別五',
		'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/arrow-down.png',
		'defaultActivate': True,
		'subDisplayGroups':[
				{
					'id': '0ab0328e-e261-4fa0-a889-7ff2cb3b8e9b',
					'name': '類別五',
					'icon': 'https://s3.ap-northeast-2.amazonaws.com/fungogowebsite/Font-Awesome-SVG-PNG-master/white/png/128/arrow-down.png',
					'defaultActivate': True
				}
			]
		}
	]
	return jsonify(filters)	

@app.route("/"+app.config['API_VERSION']+"/places", methods=['GET'])
def places():
	places = [		
		{
		'id': '21ebb1dc-bd45-42c5-bfb2-c4e6fa5f2b48',
		'title': '隱者咖打車',
		'location': { 
			'lat':24.1477999,
			'lng':120.6631362
		},
		'icon-url': 'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/995d9090-e554-4516-9409-c43d8597dfd2.png',
		'path': None,
		'displayGroups':[
				{
					'subDisplayGroupId':'a3079e3b-10c6-4274-a3e1-b36406bc552e',
					'displayGroupId':'9beb08c9-5069-4cfb-8ff9-ce8f5fbf4c07'
				},
				{
					'subDisplayGroupId':'0ab0328e-e261-4fa0-a889-7ff2cb3b8e9b',
					'displayGroupId':'28bc0fe3-aa1c-4474-8258-6f29c430562b'
				}
			]
		},
		{
		'id': '788b7823-8a60-42a1-b1b5-2987ff145d43',
		'title': '車打咖者隱',
		'location': { 
			'lat':24.147810,
			'lng':120.6631362
		},
		'icon-url': 'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/ca9f423d-9321-483e-bbd1-e7410b4f650f.jpg',
		'path': None,
		'displayGroups':[
				{
					'subDisplayGroupId':'22f443ea-1ece-469a-9633-9ed2bff3b0ff',
					'displayGroupId':'8c29988c-e5e3-4bb1-9f5e-b3f9b35410fd'
				}				
			]
		},
		{
		'id': 'bd2cdcc8-615e-44f5-8650-b8ee51258829',
		'title': '自訂路線一',
		'location': None,
		'icon-url': 'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/7a5ef23e-9863-4c69-b0f3-c77426abbc83.jpg',
		'path': 'color:0xff0000ff|weight:5|24.147810,120.6631362|24.148811,120.6632562|24.143811,120.6634762|24.149814,120.668962',
		'displayGroups':[
				{
					'subDisplayGroupId':'0ab0328e-e261-4fa0-a889-7ff2cb3b8e9b',
					'displayGroupId':'28bc0fe3-aa1c-4474-8258-6f29c430562b'
				}				
			]
		},
		{
		'id': 'e310f53e-0023-4a33-8b5c-12a7e71ecb8c',
		'title': '自訂路線二',
		'location': None,
		'icon-url': 'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/1603dc4c-f0fe-4e1d-bf69-6bdd4aa9268e.jpg',
		'path': '0x5199c9ff|weight:5|24.147813,120.6631362|24.147815,120.6633363|24.149815,120.6634364|24.141815,120.669138',
		'displayGroups':[
				{
					'subDisplayGroupId':'7d36e9ad-f2b1-475b-a4dc-f938b4c61ef6',
					'displayGroupId':'8c29988c-e5e3-4bb1-9f5e-b3f9b35410fd'
				}				
			]
		}
	]
	return jsonify(places)					
			
@app.route("/"+app.config['API_VERSION']+"/place", methods=['GET'])
def place():
	id = request.args.get('id')
	placeLocation = {
		'id': '21ebb1dc-bd45-42c5-bfb2-c4e6fa5f2b48',
		'title': '隱者咖打車',
		'description': '馬丁‧路德說過一句話：<a href="xxx.html">out link</a><br/><br/>“人生最長久的且迫切的問題是：你在為別人做什麼？”<br/>一個小動作對你來說可能沒什麼，可是做了其實會有很大的不同！因為有了社會的關懷，有了人們的鼓勵，角落裡正在微微發光，希望發揮聚沙成塔的力量，大家一起幫助城市隱者，一起看見角落裡的微光！流落街頭是什麼滋味？你可曾想過或許哪天也被迫流浪？「小書The Small Issue」收錄了街友的生存策略，教一般人如何在街頭求生？另外也報導時下最夯的剩食議題，看街友如何在剩食餐廳把剩食變美食，以及關於街友服務機構的採訪，誰是街友的褓姆？而這些原本總是被服務、被給予的隱者們也為了小書的製作，深入食物銀行成為服務者…。這是一本與 #無家者 有關的小書，部份內容由曾經流浪街頭的街友共同參與完成。目前已經有三位隱者（兩位街友、一位獨居老人）願意擔任駐點販售員，販賣小書所得60%都歸予販售員！隱者將輪班去擺攤，歡迎大家前往購買小書，可以順便給隱者加油打氣，跟他們聊聊天喔! ➤週六文炳哥，週日小梅姐在 新手書店(三點～七點)➤週六小梅姐，週日文炳哥在 壩豆製坊(一點～五點)',
		'location': { 
			'lat':24.1477999,
			'lng':120.6631362
		},
		'icon-url': 'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/995d9090-e554-4516-9409-c43d8597dfd2.png',
		'path': None,
		'images': [
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/995d9090-e554-4516-9409-c43d8597dfd2.png',
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/ca9f423d-9321-483e-bbd1-e7410b4f650f.jpg',
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/1603dc4c-f0fe-4e1d-bf69-6bdd4aa9268e.jpg',
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/3b041ad4-5f55-4768-a1e6-24546a094f25.jpg',
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/7a5ef23e-9863-4c69-b0f3-c77426abbc83.jpg'
		],
		'fields':[
			{ 
				'title':'景點地名',
				'content': '新手書店'
			},
			{ 
				'title':'景點地址',
				'content': '403台灣台中市西區向上北路129號'
			},
			{ 
				'title':'行前必讀、適合對象',
				'content': '/ 付款說明 /現金'
			},
			{ 
				'title':'服務開始時間',
				'content': '15:00'
			},
			{
				'title':'服務時長',

				'content': '240 分鐘'
			}
		],
		'displayGroups':[
				{
					'subDisplayGroupId':'a3079e3b-10c6-4274-a3e1-b36406bc552e',
					'displayGroupId':'9beb08c9-5069-4cfb-8ff9-ce8f5fbf4c07'
				},
				{
					'subDisplayGroupId':'0ab0328e-e261-4fa0-a889-7ff2cb3b8e9b',
					'displayGroupId':'28bc0fe3-aa1c-4474-8258-6f29c430562b'
				}
			]
	}
	if id == '21ebb1dc-bd45-42c5-bfb2-c4e6fa5f2b48':
		return jsonify(placeLocation)
	elif id == '788b7823-8a60-42a1-b1b5-2987ff145d43':
		placeLocation["id"] = '788b7823-8a60-42a1-b1b5-2987ff145d43'
		placeLocation["title"] = '車打咖者隱'
		placeLocation["images"] = ['https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/ca9f423d-9321-483e-bbd1-e7410b4f650f.jpg'];
		placeLocation["icon-url"] = 'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/ca9f423d-9321-483e-bbd1-e7410b4f650f.jpg';
		placeLocation["displayGroups"] = [
				{
					'subDisplayGroupId':'22f443ea-1ece-469a-9633-9ed2bff3b0ff',
					'displayGroupId':'8c29988c-e5e3-4bb1-9f5e-b3f9b35410fd'
				}				
			]
		placeLocation["location"] = { 
			'lat':24.1479020,
			'lng':120.6631362
		}
		return jsonify(placeLocation)
	elif id == 'bd2cdcc8-615e-44f5-8650-b8ee51258829':
		placeLocation["id"] = 'bd2cdcc8-615e-44f5-8650-b8ee51258829'
		placeLocation["title"] = '自訂路線一'
		placeLocation["images"] = [
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/7a5ef23e-9863-4c69-b0f3-c77426abbc83.jpg',
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/995d9090-e554-4516-9409-c43d8597dfd2.png',
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/3b041ad4-5f55-4768-a1e6-24546a094f25.jpg',
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/ca9f423d-9321-483e-bbd1-e7410b4f650f.jpg',					
			'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/7a5ef23e-9863-4c69-b0f3-c77426abbc83.jpg'
		];
		placeLocation["location"] = None
		placeLocation["path"] = 'color:0xff0000ff|weight:5|24.147810,120.6631362|24.148811,120.6632562|24.143811,120.6634762|24.149814,120.668962'
		placeLocation["icon-url"] = 'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/7a5ef23e-9863-4c69-b0f3-c77426abbc83.jpg';
		placeLocation["displayGroups"] = [
				{
					'subDisplayGroupId':'0ab0328e-e261-4fa0-a889-7ff2cb3b8e9b',
					'displayGroupId':'28bc0fe3-aa1c-4474-8258-6f29c430562b'
				}				
			]
		return jsonify(placeLocation)
	else:	
		placeLocation["id"] = 'e310f53e-0023-4a33-8b5c-12a7e71ecb8c'
		placeLocation["title"] = '自訂路線二'
		placeLocation["images"] = ['https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/1603dc4c-f0fe-4e1d-bf69-6bdd4aa9268e.jpg'];
		placeLocation["location"] = None
		placeLocation["path"] = '0x5199c9ff|weight:5|24.147813,120.6631362|24.147815,120.6633363|24.149815,120.6634364|24.141815,120.669138'
		placeLocation["icon-url"] = 'https://s3.ap-northeast-2.amazonaws.com/fungogouser/funstore/1603dc4c-f0fe-4e1d-bf69-6bdd4aa9268e.jpg';
		placeLocation["displayGroups"] = [
				{
					'subDisplayGroupId':'7d36e9ad-f2b1-475b-a4dc-f938b4c61ef6',
					'displayGroupId':'8c29988c-e5e3-4bb1-9f5e-b3f9b35410fd'
				}				
			]
		
		return jsonify(placeLocation)
		