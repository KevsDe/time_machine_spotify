from service.web_scraping import web_scraping
from service.verification import in_range_verification, format_verification
from service.spotify import SpotifyApi

URL = "https://www.billboard.com/charts/hot-100/"
user_input = input("Select the day with the following format 'YY'-'MM'-'DD': ")
year = user_input.split("-")[0]

the_hot_100 = None
artists = None

if format_verification(user_input):
    if in_range_verification(user_input):
        the_hot_100, artists = web_scraping(user_input, URL)

spot_api = SpotifyApi()
spot_api.get_uri_list(the_hot_100, artists)
spot_api.create_play_list(user_input)
spot_api.add_tracks_to_play_list()


