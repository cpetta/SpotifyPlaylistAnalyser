from auth import Auth

class Album:
	def __init__(self, auth:Auth, id:str) -> None:
		self.id:str = id
