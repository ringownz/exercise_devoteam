import json
import requests  # useless import when there's fastapi requests
from ..model.Episode import Episode

url = 'https://www.omdbapi.com/?'


def setup_url():
    f = open("../../apikey.json")
    data = json.load(f)
    return url + 't=' + data['title'] + '&apikey=' + data['apikey']


def get_episodes():
    final_url = setup_url()

    # DONE: Make request to get nr seasons
    response_json = requests.get(final_url).json()
    totalSeasons = int(response_json['totalSeasons'])

    # DONE: Obter toda a informação dos episodios para cada season.
    for season in range(1, totalSeasons + 1):
        url_each_season = final_url + '&Season=' + season
        response_season_json = requests.get(url_each_season).json()

        list_episodes_each_season = response_season_json['Episodes']
        for each in list_episodes_each_season:
            print("S" + str(season) + " E" + each["Episode"] + " : " + each["Title"])
            episode = Episode(each["imdbID"], each["Title"], each["Released"], season, int(each["Episode"]))
            episode.set_rating(float(each["imdbRating"]))

            # TODO: Save info in BD
            #  save.(imdbID: , Title, Released, Rating, Episode = Episode, Season = season)


def get_episode_info(episode_id):
    # data = db.find(episode_id)
    # data_to_user = mapper.show_user(data)      # data_to_user : id title rating S0X EX
    return None
