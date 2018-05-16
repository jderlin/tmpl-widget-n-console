import json
from os import path
import pprint
import hashlib
import logging
import requests

# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__))))
# from .enums import TAGS

logger = logging.getLogger(__name__)
pp = pprint.PrettyPrinter(indent=4)

# load enums
import json
path = path.join(path.dirname(path.realpath(__file__)), 'enums/tags.json')
with open(path, encoding="utf8") as f:
    TAGS = json.load(f)

class Fungogo(object):
	def __init__(self, webApiServer, funstoreId, vendorToken):
		super(Fungogo, self).__init__()
		self.webApiServer = webApiServer
		self.funstoreId = funstoreId
		self.vendorToken = vendorToken
		self.requestHeader = {
				'x_Vendor_Authorize': self.vendorToken,
				'x_Vendor_FunStore_Authorize': self.funstoreId
			}

	def getPrivateAttractionList(self):
		r = requests.get('%s/FunStore/%s/ExclusivePOIs' % (self.webApiServer, self.funstoreId),
			headers = self.requestHeader)
		response = r.json()
		print(r.url)

		# pp.pprint(response)
		return response

	def getPrivateAttraction(self, compId, langId):
		r = requests.get('%s/ExclusivePOIs/%s?targetLanguageId=%s' % (self.webApiServer, compId, langId),
			headers = self.requestHeader)

		response = r.json()

		information = response.get('information', [])
		if len(information):
			attributes = information[0].get('attributes', [])
			attributesDict = {}
			for row in attributes:
				attributesDict[str(row['attributeId'])] = row['value']
			response['information'][0]['attributes'] = attributesDict

			# print('update', attributesDict)

		# pp.pprint(response)
		return response

	# constancts
	def getTagText(tagId, lang='zhtw'):
		return TAGS.get(str(tagId), {}).get(lang, None)

	langId2Lang = {
		'3': 'zh-TW',
		'5': 'zh-CN',
		'6': 'en-US',
		'8': 'ja-JP',
	}

	def getLang(langId):
		return Fungogo.langId2Lang.get(str(langId))
