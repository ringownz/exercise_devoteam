import random

from fastapi.testclient import TestClient

from src import db_context
from src.main import app

client = TestClient(app)




def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_get_episodes():
    response = client.get("/api/episodes/")
    assert len(response.json()) == 73 # episodes added
    assert response.status_code == 201
    random_ep_pos = random.randint(1, 73)
    episode_info = response.json()[random_ep_pos]
    episode_id = episode_info["imdb_id"]

    response = client.get("/api/episodes/" + episode_id)
    assert response.status_code == 200
    assert response.json()["title"] == episode_info["title"]
    assert response.json()["season"] == episode_info["season"]
    assert response.json()["episode"] == episode_info["episode"]
    assert response.json()["imdb_rating"] == episode_info["imdb_rating"]
    assert response.json() == {
            "imdb_id": episode_id,
            "title": episode_info["title"],
            "season": episode_info["season"],
            "episode": episode_info["episode"],
            "imdb_rating": episode_info["imdb_rating"]
        }

def test_filter_episodes():
#    response = client.get("/api/episodes/")
#    assert len(response.json()) == 73  # episodes added

    best_eps_in_season = 5
    response = client.get("/api/episodes/filter/", params={"season": best_eps_in_season})
    assert response.status_code == 200
    assert len(response.json()) == 4
