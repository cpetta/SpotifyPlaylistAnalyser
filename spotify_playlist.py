import re
import requests
import json

from spotify_auth import Auth
from spotify_access_token import Token

class Playlist:
	def __init__(self, auth: Auth, url: str):
		self.url:str = url
		self.id:str = self.get_id()
		self.token:Token = auth.token
		self.artists:dict[str, str] = self.get_playlist_artists()

	def get_id(self) -> str:
		if not self.check_url(self.url):
			return ""

		slugs = self.url.split("/")
		slugs_last = len(slugs) - 1
		id_slug = slugs.pop(slugs_last)
		id = id_slug.split("?")[0]
		return id

	def get_playlist_artists(self) -> dict[str, str]:
		artists = {}

		if(len(self.id) == 0):
			return artists
		
		API_endpoint = f'https://api.spotify.com/v1/playlists/{self.id}'
		
		headers = {
			"Authorization": f"{self.token.token_type} {self.token.access_token}"
		}
		
		parameters = {
			"market": "US",
			"fields": "tracks.items.track.artists(name, id)"
		}

		response = requests.get(url=API_endpoint, headers=headers, params=parameters)

		tracks = response.json()['tracks']['items']

		for track in tracks:
			for artist in track['track']['artists']:
				id:str = artist['id']
				name:str = artist['name']
				artists[id] = name
		return artists

	@staticmethod
	def check_url(url: str) -> bool:
		pattern = "https:\/\/open\.spotify\.com\/playlist\/"
		is_spotify_playlist = re.match(pattern, url)

		if(is_spotify_playlist):
			return True
		else:
			return False

