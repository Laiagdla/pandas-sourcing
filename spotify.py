import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# create an app in developers.spotify.com for creating client id, and secret key.
cid = '###' # Your client id
secret = '###'  # Your secret key
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def spotify_search(artist_name,song_name):
    response = sp.search(q=artist_name + song_name, type='track', limit=1)
    return response
