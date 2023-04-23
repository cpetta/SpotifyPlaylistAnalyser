import re
import spotify_api

from auth import Auth
from artist import Artist
from album import Album


class Playlist:
	def __init__(self, auth:Auth, url:str):
		self.url:str = url
		self.id:str = self.get_id()
		self.data:dict = spotify_api.get_playlist(auth, self.id)
		self.albums:dict[str, Album] = self.get_playlist_albums()
		self.artists:dict[str, Artist] = self.get_playlist_artists()
		self.genres:list = self.get_playlist_genres()

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

		if(self.id == ""):
			return artists
		
		tracks = self.data['tracks']['items']

		for track in tracks:
			for trackArtist in track['track']['artists']:
				id:str = trackArtist['id']
				name:str = trackArtist['name']

				artist:Artist = Artist(id, name)
				artists[id] = artist
		return artists


	def get_playlist_albums(self) -> dict[str, Album]:
		albums:dict[str, Album] = {}

		if(self.id == ""):
			return albums
		
		tracks = self.data['tracks']['items']

		for track in tracks:
			for trackAlbumID in track['track']['album'].values():
				albums[trackAlbumID] = Album(trackAlbumID)
				# id:str = trackAlbum.id

		return albums


	def get_playlist_genres(self) -> list:
		
		tracks = self.data['tracks']['items']

		# Get each Album Genre
		for track in tracks:
			break

		
		self.data['tracks']['items']
		

		# get each Artist Genre

		return []

	@staticmethod
	def check_url(url:str) -> bool:
		pattern = "https:\/\/open\.spotify\.com\/playlist\/"
		is_spotify_playlist = re.match(pattern, url)

		if(is_spotify_playlist):
			return True
		else:
			return False

