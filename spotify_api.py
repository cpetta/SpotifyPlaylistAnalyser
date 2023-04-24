import requests
import math
import logging

from auth import Auth

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)

retry_strategy = Retry(
	total=3,
	status_forcelist=[429, 500, 502, 503, 504],
	method_whitelist=["GET"],
	backoff_factor = 16
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)



@staticmethod
def get_related_artists(auth:Auth, artist):
	API_endpoint = f'https://api.spotify.com/v1/artists/{artist.id}/related-artists'

	response = http.get(url=API_endpoint, headers=auth.http_headers()) # type: ignore

	return response.json()['artists']



@staticmethod
def get_playlist(auth:Auth, id:str):
	API_endpoint = f'https://api.spotify.com/v1/playlists/{id}'
	
	parameters = {
		"market": "US",
		"fields": "tracks.items.track.artists(name, id), tracks.items.track.album(id)"
	}

	response = http.get(url=API_endpoint, headers=auth.http_headers(), params=parameters) # type: ignore

	return response.json()



@staticmethod
def get_several_artists_genres(auth:Auth, id_list:list[str]) -> dict[str, int]:
	genres:dict[str, int] = {}

	API_endpoint = f'https://api.spotify.com/v1/artists'


	#split artist info requests into groups of 50
	limit:int = 2
	split_requests = []

	num_requests = math.ceil(len(id_list) / limit)

	for x in range(num_requests):
		split_requests.append([])

	i:int = 0
	counter:int = 0
	
	for id in id_list:
		counter += 1
		if counter > limit:
			i += 1
			counter = 0

		split_requests[i].append(id)


	for request in tqdm(split_requests):
		ids:str = ','.join(request)
		
		if(ids == ""):
			continue

		parameters = {
			"ids": ids
		}

		response = http.get(url=API_endpoint, headers=auth.http_headers(), params=parameters)
		
		data = response.json()
		for artists in data.values():
			for artist in artists:
				for genre in artist['genres']:
					if genre in genres:
						genres[genre] += 1
					else:
						genres[genre] = 1
		
	return genres



@staticmethod
def get_album_genre(auth:Auth, id:str) -> list[str]:
	
	API_endpoint = f'https://api.spotify.com/v1/albums/{id}'

	response = http.get(url=API_endpoint, headers=auth.http_headers())

	return response.json()['genres']