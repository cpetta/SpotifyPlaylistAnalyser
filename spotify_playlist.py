import re
import requests
import json

from spotify_auth import Auth
from artist import Artist
from spotify_access_token import Token

class Playlist:
	def __init__(self, auth:Auth, url:str):
		self.url:str = url
		self.id:str = self.get_id()
		self.auth:Auth = auth
		self.artists:dict[str, Artist] = self.get_playlist_artists()

	def get_id(self) -> str:
		if not self.check_url(self.url):
			return ""

		slugs:list[str] = self.url.split("/")
		slugs_last:int = len(slugs) - 1
		id_slug:str = slugs.pop(slugs_last)
		id:str = id_slug.split("?")[0]
		return id

	def get_playlist_artists(self) -> dict[str, Artist]:
		artists:dict[str, Artist] = {}

		if(len(self.id) == 0):
			return artists
		
		API_endpoint = f'https://api.spotify.com/v1/playlists/{self.id}'
		
		parameters = {
			"market": "US",
			"fields": "tracks.items.track.artists(name, id)"
		}

		response = requests.get(url=API_endpoint, headers=self.auth.http_headers(), params=parameters) # type: ignore

		tracks = response.json()['tracks']['items']

		for track in tracks:
			for trackArtist in track['track']['artists']:
				id:str = trackArtist['id']
				name:str = trackArtist['name']

				artist:Artist = Artist(id, name)
				artists[id] = artist
		return artists

	def get_playlist_genres(self) -> list:
		# TODO implement logic for going through list of artists and getting genres
		return []

	@staticmethod
	def check_url(url:str) -> bool:
		pattern = "https:\/\/open\.spotify\.com\/playlist\/"
		is_spotify_playlist = re.match(pattern, url)

		if(is_spotify_playlist):
			return True
		else:
			return False

