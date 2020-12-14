# Took https://github.com/corpetty/py-etherscan-api as a learning experience.

import requests
import collections

class Client(object):

	PREFIX = 'https://api.etherscan.io/api?'
	ADDRESS = '&address='
	API_KEY = '&apikey='

	def __init__(self, API_KEY = ''):
		# Allows persistent cookies.
		self.http = requests.session()

		# For constructing the URL. 
		self.url_dict = collections.OrderedDict([
			(self.ADDRESS, '')
			(self.API_KEY, API_KEY),
			])

		self.url = None


	def build_url(self):
		# Creates a URL based on the values given to it in self.url_dict. 
		self.url = self.PREFIX + ''.join(
			[param + val if val else '' for param, val in self.url_dict.items()]
			)

	def connect(self):
		try:
			request = self.http.get(self.url)
		except requests.exceptions.ConnectionError:
			print('Connection Refused')

		if request.status_code == 200:
			if request.text:
				data = request.json()
				status = data.get('status')
				if status == '1':
					return data
				else:
					print('Empty Response')
		else:
			print('Bad Request')


	def show_api_key(self):
		print(self.url_dict)

		


		
