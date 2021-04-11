from dotenv import load_dotenv, find_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(find_dotenv())
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


class SpotifyApi:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                            client_secret=CLIENT_SECRET,
                                                            redirect_uri="http://localhost",
                                                            scope="playlist-modify-public",
                                                            cache_path="../token.txt",
                                                            show_dialog=True))
        self.user_id = self.sp.current_user()["id"]
        self.uri_list = []
        self.play_list_id = None

    def get_uri_list(self, song_list, artists_list):
        """Create a list with the URI obtained with a song and an artist"""
        for song in range(len(song_list)):
            track_info = self.sp.search(q=f"track:{song_list[song]} artist:{artists_list[song]}")
            try:
                self.uri_list.append(track_info.get("tracks").get("items")[0].get("uri"))

            except IndexError:
                print(f'The song {song_list[song]} by {artists_list[song]}was not found so it was skipped')

    def create_play_list(self, user_input):
        """Creates a playlist"""
        play_list_id = self.sp.user_playlist_create(
            user=self.user_id,
            name=f"100 top from {user_input}",
            public=True,
            collaborative=False,
        )
        self.play_list_id = play_list_id["id"]

    def add_tracks_to_play_list(self):
        """Add tracks to the playlist"""
        self.sp.playlist_add_items(
            playlist_id=self.play_list_id,
            items=self.uri_list)
