import re
import requests

from spotify_auth import Auth

class Playlist:
	def __init__(self, ui):
		self.url = ui.url
		self.id = self.get_id()
		# self.data = self.get_data()

	def get_id(self):
		if self.check_url(self.url):
			slugs = self.url.split("/")
			slugs_last = len(slugs) - 1
			id_slug = slugs.pop(slugs_last)

			id = id_slug.split("?")[0]

			self.id = id


	def get_data(self):
		API_endpoint = 'https://api.spotify.com/v1/playlists/'
		# parameters = {
		# 	"key" : value,
		# 	"type": "multiple"
		# }
		# response = requests.get(url=API_endpoint, params = parameters)

		headers = {
			"Authorization": ""
		}

		# response = requests.get(url=API_endpoint, headers=headers)
		# playlist_data = response.json()["results"]

	@staticmethod
	def check_url(url):
		pattern = "https:\/\/open\.spotify\.com\/playlist\/"
		is_spotify_playlist = re.match(pattern, url)

		if(is_spotify_playlist):
			return True
		else:
			return False

