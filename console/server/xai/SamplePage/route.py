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

@app.route("/"+app.config['API_VERSION']+"/filters", methods=['GET'])
def filters():
	filters = [
		{
		'id': '9beb08c9-5069-4cfb-8ff9-ce8f5fbf4c07',
		'name': '餐廳',
		'icon': '日式',
		'defaultActivate': False,
		'childrens':[
				{
					'id': 'a3079e3b-10c6-4274-a3e1-b36406bc552e',
					'name': '中式',
					'icon': '日式',
					'defaultActivate': False
				},
				{
					'id': '34d6cf27-de11-4504-a980-32d9dcccdfc2',
					'name': '美式',
					'icon': '日式',
					'defaultActivate': False
				},
				{
					'id': 'a1365f37-bcb4-4183-adf3-26a83209b806',
					'name': '日式',
					'icon': '日式',
					'defaultActivate': False
				}
			]
		},
		{
		'id': 'f07bdd19-c156-4ad7-a296-e7f1c967ba5a',
		'name': '鳥類',
		'icon': '日式',
		'defaultActivate': False,
		'childrens':[
				{
					'id': '358e74bf-a2a7-40d5-8e4b-6e8a30f1459f',
					'name': '中式',
					'icon': '日式',
					'defaultActivate': True
				},
				{
					'id': '4dc5e881-48da-4fcc-8d76-e039d02e5f8f',
					'name': '美式',
					'icon': '日式',
					'defaultActivate': True
				},
				{
					'id': 'edfdccbd-d273-4124-aa27-4cd8409dd41d',
					'name': '日式',
					'icon': '日式',
					'defaultActivate': False
				}
			]
		},
		{
		'id': '8c29988c-e5e3-4bb1-9f5e-b3f9b35410fd',
		'name': '類別一',
		'icon': '日式',
		'defaultActivate': False,
		'childrens':[
				{
					'id': 'eedb5172-2a14-48c0-983d-256422b0fe49',
					'name': '中式',
					'icon': '日式',
					'defaultActivate': False
				},
				{
					'id': '7d36e9ad-f2b1-475b-a4dc-f938b4c61ef6',
					'name': '美式',
					'icon': '日式',
					'defaultActivate': False
				},
				{
					'id': '22f443ea-1ece-469a-9633-9ed2bff3b0ff',
					'name': '日式',
					'icon': '日式',
					'defaultActivate': False
				}
			]
		},
		{
		'id': 'ccb81ab5-6f50-4d2b-ad62-e3c54018364a',
		'name': '類別二',
		'icon': '日式',
		'defaultActivate': True
		},
		{
		'id': 'a4d5b6c8-dc45-4763-8e54-8e0519444847',
		'name': '類別三',
		'icon': '日式',
		'defaultActivate': False
		},
		{
		'id': '404d398f-7520-4460-be22-629c30899d1c',
		'name': '類別四',
		'icon': '日式',
		'defaultActivate': False
		},
		{
		'id': '28bc0fe3-aa1c-4474-8258-6f29c430562b',
		'name': '類別五',
		'icon': '日式',
		'defaultActivate': True
		}
	]
	return jsonify(filters)	

@app.route("/"+app.config['API_VERSION']+"/places", methods=['POST'])
def places():
	places = [		
		{
		'id': '36c4c67e-183c-4fb9-b95c-0f37a65953c5',
		'title': '類別二',
		'location': '日式',
		'icon-url': True,
		'path': True,
		'images': [],
		'fields':[]
		},
		{
		'id': 'ce96991e-d65f-4b6b-9a38-2dfd6b52ef68',
		'title': '類別二',
		'location': '日式',
		'icon-url': True,
		'path': True,
		'images': [],
		'fields':[]
		},
		{
		'id': '21ebb1dc-bd45-42c5-bfb2-c4e6fa5f2b48',
		'title': '類別二',
		'location': '日式',
		'icon-url': True,
		'path': True,
		'images': [],
		'fields':[]
		},
		{
		'id': 'e310f53e-0023-4a33-8b5c-12a7e71ecb8c',
		'title': '類別二',
		'location': '日式',
		'icon-url': True,
		'path': True,
		'images': [],
		'fields':[]
		}
	]
	return jsonify(places)					
			
@app.route("/"+app.config['API_VERSION']+"/place", methods=['GET'])
def place():
	place = {
		'id': '21ebb1dc-bd45-42c5-bfb2-c4e6fa5f2b48',
		'title': '鳥類',
		'description': 'ddd',
		'location': '日式',
		'icon-url': True,
		'path': True,
		'images': [],
		'fields':[]
	}
	return jsonify(place)	