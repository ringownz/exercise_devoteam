from src.main import app
from src.services import episodeService as service

######     NOT WORKING
### N_EEEDS UPDATE
###

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

