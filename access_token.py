import json
import requests
import time

class Token:
	def __init__(
			self,
			access_token:str = "",
			token_type:str = "",
			expires_in:int = 0,
			expire_time:float = 0
		):
		self.access_token:str = access_token
		self.token_type:str = token_type
		self.expires_in:int = expires_in
		self.expire_time:float = expire_time

	def to_json(self) -> dict:
		return  {
			"access_token": self.access_token,
			"token_type": self.token_type,
			"expires_in": self.expires_in,
			"expire_time": self.expire_time,
		}

	def load_saved(self) -> bool:
		try: 
			f = open("token.json", "r")
			data:str = f.readline()
			f.close()
			saved_auth = json.loads(data, object_hook=lambda d: Token(**d))
			
			self.access_token:str = saved_auth.access_token
			self.token_type:str = saved_auth.token_type
			self.expires_in:int = saved_auth.expires_in
			self.expire_time:float = saved_auth.expire_time
			return True
		except:
			return False

	def save(self) -> bool:
		try:
			file = open("token.json", "w+")
			token_json = json.dumps(self.to_json())
			file.write(token_json)
			file.close()
			return True
		except:
			return False
		
	def request_new(self, id:str, secret:str) -> bool:
		try:
			data:dict[str, str] = {
				'grant_type': 'client_credentials',
				'client_id': id,
				'client_secret': secret,
			}
			response = requests.post('https://accounts.spotify.com/api/token', data=data)
			if(response.ok):
				new_token:Token = json.loads(response.content, object_hook=lambda d: Token(**d))
				current_time:float = time.mktime(time.localtime())

				self.access_token:str = new_token.access_token
				self.token_type:str = new_token.token_type
				self.expires_in:int = new_token.expires_in
				self.expire_time:float = current_time + new_token.expires_in

				self.save()

				return True
			else:
				return False
		except:
			return False
