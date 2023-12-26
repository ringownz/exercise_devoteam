import json
import os

import requests  # useless import when there's fastapi requests
from ..model.Episode import Episode
from ..repository import episodesRepository
from ..utils import mapper
from pathlib import Path

url = 'https://www.omdbapi.com/?'


def setup_url():
    path = Path(__file__).parent / ".." / ".." / "apikey.json"
    with path.open() as f:
        f = open(path)

    data = json.load(f)
    # data = {
    #    "title": "Game of Thrones",
    #    "apikey": "76ecd78f"
    # }
    return url + 't=' + data['title'] + '&apikey=' + data['apikey']


def get_episodes():
    final_url = setup_url()

    # DONE: Make request to get nr seasons
    response_json = requests.get(final_url).json()
    totalSeasons = int(response_json['totalSeasons'])

    # DONE: Obter toda a informação dos episodios para cada season.
    for season in range(1, totalSeasons + 1):
        url_each_season = final_url + '&Season=' + str(season)
        response_season_json = requests.get(url_each_season).json()

        list_episodes_each_season = response_season_json['Episodes']
        for each in list_episodes_each_season:
            print("S" + str(season) + " E" + each["Episode"] + " : " + each["Title"])
            episode = Episode(each["imdbID"], each["Title"], each["Released"], season, each["Episode"])
            episode.set_rating(each["imdbRating"])
            episodesRepository.create_episode(episode)  # Done: save info to DB

    listOfEpisodes = []
    all_from_db = episodesRepository.get_all_episodes()
    for each in all_from_db:
        listOfEpisodes.append(mapper.show_user_from_db_by_id(each))

    return listOfEpisodes


def get_episode_info(episode_id):
    row = episodesRepository.get_episode_by_id(episode_id)
    data_to_user = mapper.show_user_from_db_by_id(row)  # data_to_user : id title rating S0X EX
    return data_to_user


def filter_episodes_by_rating(season):
    # Filter by season and rating > 8.8
    listOfEpisodes = []
    all_from_db = episodesRepository.get_episodes_by_rating(season)
    for each in all_from_db:
        listOfEpisodes.append(mapper.show_user_from_db_by_id(each))

    return listOfEpisodes
