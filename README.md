# SpotifyPlaylistAnalyser

Currently requires an additional ``settings.py`` that contains a spotify API id and secret formatted like

```
class Settings:
	def __init__(self):
		self.id:str = ""
		self.secret:str = ""
```


Usage
1. Right click a playlist in spotify
2. Select ``Share``
3. Select ``Copy Spotify URI``
4. Example: ``https://open.spotify.com/playlist/603oF0bPdW4ZwSCHF8Zs4L?si=0986791c35424fb8``
5. run ``python spotifyPlaylistAnalyser.py``
6. Paste the copied URI into the command window
7. Press Enter
