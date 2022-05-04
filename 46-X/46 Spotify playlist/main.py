from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "affde56478cd4519b0ad9d4f7b9f6108"
SPOTIFY_SECRET = "57836d84021340038210f8e3593e148b"
URI = "http://example.com"

date = input("What year do you want to go to?(YYYY-MM-DD): ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

song_tags = soup.find_all(name="h3", class_="a-no-trucate")

songs = [song_tag.getText() for song_tag in song_tags]

better_list = [what.replace("\n","") for what in songs]
even_better = [what.replace("\t","") for what in better_list]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in even_better:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)