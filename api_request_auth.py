import requests
import csv
import json
from base64 import b64encode

def call_api_with_auth(id, page_id, auth):
	
	try:
		userAndPass = b64encode(bytes(auth, "utf-8")).decode("ascii")
		response = requests.get(
			url="https://moderation-api.visenze.com/v2/taggedimgs/{id}/".format(id = id),
			headers={
				'Content-Type': 'application/json',
  				'Authorization' : 'Basic %s' %  userAndPass,
			},
			params={
				'limit': 100,
				'page': page_id,
				'show_product': "true"
			}
		)	
		print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
		# print('Response HTTP Response Body: {content}'.format(content=response.content))
		return response
	except requests.exceptions.RequestException as e:
		print('HTTP request failed: {content}'.format(content=e))

def main():
    id="dd"
    pageid="dd"
    auth="user:pass"
    response = json.loads(call_api_with_auth(id, pageid, auth).text)