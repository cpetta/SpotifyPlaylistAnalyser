import spotify_api

from auth import Auth

class Artist:
	def __init__(self, id:str, name:str) -> None:
		self.id:str = id
		self.name:str = name
		self.count:int = 1
		self.generes:dict = {}
		self.related_artists:dict[str, 'Artist'] = {}

	def get_related_artists(
			self,
			auth:Auth,
			artists:dict[str, 'Artist'] = {}
		) -> dict[str, 'Artist']:
		

		if(len(self.id) == 0):
			return artists

		data = spotify_api.get_related_artists(auth, self)

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

	# Compairison opperators
	# Equal
	def __eq__(self, other: 'Artist') -> bool:
		return self.count == other.count
	
	# Greater Than	
	def __gt__(self, other: 'Artist') -> bool:
		return self.count < other.count
	
	# Greater or equal
	def __ge__(self, other: 'Artist') -> bool:
		return self.count <= other.count

	# Less then
	def __lt__(self, other: 'Artist') -> bool:
		return self.count > other.count
	
	# Less than or equal
	def __le__(self, other: 'Artist') -> bool:
		return self.count >= other.count
	
	# Not equal
	def __ne__(self, other: 'Artist') -> bool:
		return self.count != other.count