
import spotify_api

from auth import Auth

class Album:
	def __init__(self, auth:Auth, id:str) -> None:
		self.id:str = id
		# Album Genre's consistantly comes back blank.
		# self.genres:list[str] = spotify_api.get_album_genre(auth, id)