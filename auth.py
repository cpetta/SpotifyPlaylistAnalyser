import sys
import time

from access_token import Token
from settings import Settings

class Auth:
	def __init__(self, settings:Settings):
		self.id:str = settings.id
		self.secret:str = settings.secret
		self.token:Token = self.get_token()

	def get_token(self) -> Token:
		token:Token = Token()
		request_new_token:bool = False
		loaded_saved_token:bool = token.load_saved()

		if(not loaded_saved_token):
			print("Unable to loaded Saved Token requesting new one")
			request_new_token = True
		else:
			current_time:float = time.mktime(time.localtime())

			if(current_time < token.expire_time):
				print("Good Token Expires in", token.expire_time - current_time)
			else:
				print("Expired token", token.expire_time - current_time)
				request_new_token = True

		if(request_new_token):
			request_success:bool = token.request_new(self.id, self.secret)
			
			if(request_success):
				print("requested new token")
			else:
				print("error requesting new token")
				sys.exit(1)

		return token

	def http_headers(self) -> dict:
		return {
			"Authorization": f"{self.token.token_type} {self.token.access_token}"
		}