import os

import uvicorn
from fastapi import FastAPI

from src import db_context
from src.services import episodeService
from src.services import commentService

app = FastAPI()
db_context.start()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/episodes/")
async def read_items():
    # Get all episodes from API
    return episodeService.get_episodes()


@app.get("/episodes/filter/")
async def filter_episodes(season: int = None):
    # Get all episodes from API
    return episodeService.filter_episodes_by_rating(season)


@app.get("/episodes/{episode_id}")
async def read_items(episode_id: str):
    # Return information about episode id in a list
    return episodeService.get_episode_info(episode_id)


@app.post("/comment/{episode_id}")
async def create_comment(episode_id: str, comment: str):
    return commentService.create_comment(episode_id, comment)


@app.get("/comment/{comment_id}")
async def get_comment(comment_id: int):
    return commentService.get_comment(comment_id)


@app.get("/comment/all/{episode_id}")
async def read_items(episode_id: str = None):
    # Return information about episode id in a list
    return commentService.get_all_comments(episode_id)


@app.post("/comment/id/{comment_id}")
async def update_comment(comment_id: int, episode_id: str, comment: str):
    return commentService.update_comment(comment_id, episode_id, comment)


@app.delete("/comment/id/{comment_id}")
async def update_comment(comment_id: int):
    return commentService.delete_comment(comment_id)


if __name__ == '__main__':
    db_context.start()
    uvicorn.run(app, port=8000)  # used to test


