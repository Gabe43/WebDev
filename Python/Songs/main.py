# # from unicodedata import name
# # import requests
# # from bs4 import BeautifulSoup
# from spotipy.oauth2 import SpotifyOAuth
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# # time = int(input('Which year do you want to travel to? Type the data in this format YYYY-MM-DD: '))

# # url = 'https://www.billboard.com/charts/hot-100/2000-08-12/'

# # songs = []
# # response = requests.get(url)
# # data = response.text
# # soup = BeautifulSoup(data,'html.parser')
# # sng = soup.select(selector='li h3')

# # for text in sng:
# #     songs.append(text.getText('h3').split('\n')[1])

# # songs = [itm for itm in songs if itm!='h3']


# acces='BQDeyB-d6Mc2hGxaIVpj1VsJQqQF6eg5kL4X2vEYSUXAcT5rr75TnXQrirWBNR0kbXZz7v2bGjGm0XstjUxS_Z1sKC974qPwgzglE4n6OQrrXfdnsBltIzxY-05irNetRiJiVpqKz_WDqqDbJJ_uTkDfPUX61kHIWancIQ'

# sp = spotipy.oauth2.SpotifyOAuth(client_id=id,client_secret=pas,redirect_uri='https://example.com/callback/',cache_path='token.txt')

# # sp.get_access_token()
# spotify = spotipy.client.Spotify(auth=acces)

# lst = 'Everythin You Want'

# result =spotify.search(q=f'track:{lst}, year:{2000}',type='track',limit=5)
# print(result)

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element_information_song")
song_names = [song.getText() for song in song_names_spans]

#Spotify Authentication

id = 'f260c2a21d1c44f8840a8b13c9a787dd'
pas = '5b0b13965f0f40c4b775fc242331be86'
user_id = '31sg3ujynlzk5dbkhcbthhygwgke'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback/",
        client_id=id,
        client_secret=pas,
        show_dialog=True,
        cache_path="token.txt"
    )
)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)