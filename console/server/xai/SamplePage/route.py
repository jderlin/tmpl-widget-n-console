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

@app.route("/"+app.config['API_VERSION']+"/test", methods=['GET'])
def test():
	return jsonify({
		'test': 'test',
		'test': 'false'
	})

@app.route("/"+app.config['API_VERSION']+"/bool", methods=['GET'])
def bool():
	stores = [{
    'name': 'Elton\'s first store',
    'items': [{'name':'my item 1', 'price': 30 }],
    'dda': True,
    },
    {
    'name': 'Elton\'s second store',
    'items': [{'name':'my item 2', 'price': 15 }],
    'dda': False,
    },
]
	return jsonify(stores)			

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
		}
	])