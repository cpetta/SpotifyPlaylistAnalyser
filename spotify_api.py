import requests

from auth import Auth


@staticmethod
def get_related_artists(auth:Auth, artist):
	API_endpoint = f'https://api.spotify.com/v1/artists/{artist.id}/related-artists'

	response = requests.get(url=API_endpoint, headers=auth.http_headers()) # type: ignore

	return response.json()['artists']


@staticmethod
def get_playlist(auth:Auth, id:str):
	API_endpoint = f'https://api.spotify.com/v1/playlists/{id}'
	
	parameters = {
		"market": "US",
		"fields": "tracks.items.track.artists(name, id), tracks.items.track.album(id)"
	}

	response = requests.get(url=API_endpoint, headers=auth.http_headers(), params=parameters) # type: ignore

	return response.json()