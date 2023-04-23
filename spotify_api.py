import requests
import math

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

@staticmethod
def get_several_artists_genres(auth:Auth, id_list:list[str]) -> list[str]:
	genres = {}

	API_endpoint = f'https://api.spotify.com/v1/artists'

	i:int = 0
	limit:int = 50
	split_requests = []

	num_requests = math.ceil(len(id_list) / limit)

	print(num_requests)

	for id in id_list:
		if i >= limit:
			i += 1
			continue

		split_requests[i].append(id)
			
	for request in split_requests:
		ids:str = ','.join(request)
		
		parameters = {
			"ids": ids
		}

		print(parameters)
		# response = requests.get(url=API_endpoint, headers=auth.http_headers())
	return []
	# return response.json()['genres']

@staticmethod
def get_album_genre(auth:Auth, id:str) -> list[str]:
	
	API_endpoint = f'https://api.spotify.com/v1/albums/{id}'

	response = requests.get(url=API_endpoint, headers=auth.http_headers())

	return response.json()['genres']