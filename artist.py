import requests

from spotify_auth import Auth

class Artist:
	def __init__(self, id:str, name:str):
		self.id:str = id
		self.name:str = name
		self.count:int = 1
		self.related_artists:dict[str, 'Artist'] = {}

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

			self.related_artists[id] = Artist(id, name)
			
			if (id in artists):
				artists[id].count += 1
			else:
				artists[id] = self.related_artists[id]

		return artists
	
	# ToString

	def __str__(self) -> str:
		return f"\nName: {self.name}\nCount: {self.count}\n"
		# return f"\nName: {self.name}\n id: {self.id}\n count:{self.count}\n"


	# Compairison opperators
	# Equal
	def __eq__(self, other: 'Artist') -> bool:
		if self.count == other.count:
			return True
		else:
			return False
	
	# Greater Than	
	def __gt__(self, other: 'Artist') -> bool:
		if self.count < other.count:
			return True
		else:
			return False
	
	# Greater or equal
	def __ge__(self, other: 'Artist') -> bool:
		if self.count <= other.count:
			return True
		else:
			return False
	
	# Less then
	def __lt__(self, other: 'Artist') -> bool:
		if self.count > other.count:
			return True
		else:
			return False
	
	# Less than or equal
	def __le__(self, other: 'Artist') -> bool:
		if self.count >= other.count:
			return True
		else:
			return False
	
	# Not equal
	def __ne__(self, other: 'Artist') -> bool:
		if self.count != other.count:
			return True
		else:
			return False