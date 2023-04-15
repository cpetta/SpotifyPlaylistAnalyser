import argparse

from spotify_playlist import Playlist

class CommandLineUI:
	def __init__(self):
		parser = argparse.ArgumentParser(description='Analyze a Spotify Playlist')
		
		parser.add_argument(
			'url',
			metavar='url',
			type=str,
			nargs=1,
			help='Share URL for the spotify playlist',
		)

		args = parser.parse_args()

		url = args.url[0]

		check_url = Playlist.check_url(url)

		if check_url:
			self.url = url
		else:
			self.url = False
			print("Please ensure that the url provided is a share link for the playlist e.x (open.spotify.com/playlist/)")