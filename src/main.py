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
async def get_episodes():
    # Get all episodes from API
    return episodeService.get_episodes()


@app.get("/episodes/filter/")
async def filter_episodes(season: int = None):
    # Get all episodes from API
    return episodeService.filter_episodes_by_rating(season)


@app.get("/episodes/{episode_id}")
async def get_episode(episode_id: str):
    # Return information about episode id in a list
    return episodeService.get_episode_info(episode_id)


@app.post("/comment/{episode_id}")
async def create_comment(episode_id: str, comment: str):
    response = commentService.create_comment(episode_id, comment)
    if response is not None:
        if type(response) == Exception:
            return response.__str__()
        return f"Comment added with id: {response}"


@app.get("/comment/{comment_id}")
async def get_comment(comment_id: int):
    return commentService.get_comment(comment_id)


@app.get("/comment/all/{episode_id}")
async def get_all_comments(episode_id: str = None):
    # Return information about episode id in a list
    return commentService.get_all_comments(episode_id)


@app.post("/comment/id/{comment_id}")
async def update_comment(comment_id: int, episode_id: str, comment: str):
    return commentService.update_comment(comment_id, episode_id, comment)


@app.delete("/comment/id/{comment_id}")
async def delete_comment(comment_id: int):
    response = commentService.delete_comment(comment_id)
    if response is None:
        return f"Comment with id {comment_id} deleted successfully"


if __name__ == '__main__':
    db_context.start()
    uvicorn.run(app, port=8000)  # used to test


