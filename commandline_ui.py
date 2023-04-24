import argparse
import sys

from playlist import Playlist

class CommandLineUI:
	def __init__(self):
		parser = argparse.ArgumentParser(description='Analyze a Spotify Playlist')
		
		self.url = ""

		parser.add_argument(
			'url',
			metavar='url',
			type=str,
			nargs=1,
			help='Share URL for the spotify playlist',
		)

		try:
			args = parser.parse_args()
			
			url:str = args.url[0]

			check_url = Playlist.check_url(url)

			if check_url:
				self.url: str = url
			else:
				self.url: str = ""
				print("Please ensure url is formatted like: (open.spotify.com/playlist/)")
		except:
			self.ask_for_url()


	def ask_for_url(self):
		while(self.url == ""):
			print("Enter a spotify playlist URL. Formatted like: (open.spotify.com/playlist/)")
			url = input("URL: ")

			check_url = Playlist.check_url(url)

			if check_url:
				self.url: str = url
			elif(url == "quit"):
				sys.exit(0)
			else:
				self.url: str = ""
				print(f"url doesn't appear to be the correct format. Should resemble:(open.spotify.com/playlist/)")
