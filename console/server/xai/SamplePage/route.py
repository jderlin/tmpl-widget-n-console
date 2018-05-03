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
	return jsonify([
		{
		'id': '9beb08c9-5069-4cfb-8ff9-ce8f5fbf4c07',
		'name': '餐廳',
		'icon': '日式',
		'defaultActivate': false,
		'childrens':[
				{
					'id': 'a3079e3b-10c6-4274-a3e1-b36406bc552e',
					'name': '中式',
					'icon': '日式',
					'defaultActivate': false
				},
				{
					'id': '34d6cf27-de11-4504-a980-32d9dcccdfc2',
					'name': '美式',
					'icon': '日式',
					'defaultActivate': true
				},
				{
					'id': 'a1365f37-bcb4-4183-adf3-26a83209b806',
					'name': '日式',
					'icon': '日式',
					'defaultActivate': false
				}
			]
		},
		{
		'id': 'f07bdd19-c156-4ad7-a296-e7f1c967ba5a',
		'name': '鳥類',
		'icon': '日式',
		'defaultActivate': false,
		'childrens':[
				{
					'id': '358e74bf-a2a7-40d5-8e4b-6e8a30f1459f',
					'name': '中式',
					'icon': '日式',
					'defaultActivate': false
				},
				{
					'id': '4dc5e881-48da-4fcc-8d76-e039d02e5f8f',
					'name': '美式',
					'icon': '日式',
					'defaultActivate': true
				},
				{
					'id': 'edfdccbd-d273-4124-aa27-4cd8409dd41d',
					'name': '日式',
					'icon': '日式',
					'defaultActivate': false
				}
			]
		}
	])	

@app.route("/"+app.config['API_VERSION']+"/places", methods=['POST'])
def places():
	return jsonify({
		'test': 'test'
	})				
			
@app.route("/"+app.config['API_VERSION']+"/place", methods=['GET'])
def place():
	return jsonify({
		'test': 'test'
	})	