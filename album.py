
class Album:
	def __init__(self, id:str) -> None:
		self.id:str = id
		self.genres:list = self.get_genres()


	def get_genres(self) -> list:
		return []