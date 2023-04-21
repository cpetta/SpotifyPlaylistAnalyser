import requests

from spotify_auth import Auth

class Artist:
	def __init__(self, id:str, name:str):
		self.id:str = id
		self.name:str = name
		self.count:int = 1

	def get_related_artists(
			self,
			auth:Auth,
			artists:dict[str, 'Artist'] = {}
		) -> dict[str, 'Artist']:
		

		if(len(self.id) == 0):
			return artists
		
		API_endpoint = f'https://api.spotify.com/v1/artists/{self.id}/related-artists'

		response = requests.get(url=API_endpoint, headers=auth.http_headers()) # type: ignore

		data = response.json()['artists']

		for item in data:
			id:str = item['id']
			name:str = item['name']
			
			if (id in artists):
				artists[id].count += 1
			else:
				artists[id] = Artist(id, name)

		return artists
	
	def __str__(self) -> str:
		return f" Name: {self.name}\n id: {self.id}\n count:{self.count}"