import argparse
import sys

from spotify_playlist import Playlist

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
				print("Please ensure that the url provided is a share link for the playlist e.x (open.spotify.com/playlist/)")
		except:
			self.ask_for_url()


	def ask_for_url(self):
		while(self.url == ""):
			print("Please enter a spotify playlist share URL. Formatted such as: (open.spotify.com/playlist/)")
			url = input("URL: ")

			check_url = Playlist.check_url(url)

			if check_url:
				self.url: str = url
			elif(url == "quit"):
				sys.exit(0)
			else:
				self.url: str = ""
				print(f"url doesn't appear to be the correct format. Please make sure it looks similar to (open.spotify.com/playlist/)")
