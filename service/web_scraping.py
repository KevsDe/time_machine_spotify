from bs4 import BeautifulSoup
import requests


def web_scraping(user_input, url):
    """Returns a list of song and a list of artist from billboard.com"""
    url = url + user_input
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.text

    soup = BeautifulSoup(data, "html.parser")
    songs_soup = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
    artist_soup = soup.find_all(name="span", class_="chart-element__information__artist "
                                                    "text--truncate color--secondary")

    songs = [songs_soup[x].getText() for x in range (len(songs_soup))]
    artists = [artist_soup[x].getText() for x in range (len(artist_soup))]
    return songs, artists


