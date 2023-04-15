import requests
import json

class Auth:
	def __init__(self, settings):
		self.id = settings.id
		self.secret = settings.secret
		# self.token = self.get_saved_auth() #self.get_token()
		self.test_token = {
			"access_token": "TADA",
			"token_type": "Bearer",
			"expires_in": 3600
		}

		self.save_auth()


	def get_token(self):
		data = {
			'grant_type': 'client_credentials',
			'client_id': self.id,
			'client_secret': self.secret,
		}
		response = requests.post('https://accounts.spotify.com/api/token', data=data)
		return response


	def get_saved_auth(self):
		try: 
			f = open ("auth.json", "r")
			data = f.readlines()
			print(data)
			f.close()
		except:
			self.save_auth()
			print("Creating auth file to save auth request.")

	def save_auth(self):
		try:
			file = open("auth.json", "w+")
			Auth_json = json.dumps(self.token)
			file.write(Auth_json)
			file.close()
		except:
			print("Error writing to auth file")


