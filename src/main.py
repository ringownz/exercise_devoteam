import os

import uvicorn
from fastapi import FastAPI

from src import db_context
from src.services import episodeService as service

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/episodes/")
async def read_items():
    # Get all episodes from API
    return service.get_episodes()


@app.get("/episodes/{episode_id}")
async def read_items(episode_id: str):
    # Return information about episode id in a list
    return service.get_episode_info(episode_id)


if __name__ == '__main__':
    uvicorn.run(app, port=8000)  # used to test
#    print("Hello World!")

    # bootstrap

    # carregar db

    # ativar endpoints


db_context.create_connection("database.db")
db_context.delete_all_tables()
db_context.create_all()
