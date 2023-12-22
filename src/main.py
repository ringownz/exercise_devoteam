from fastapi import FastAPI
from src.services import omdb_service as service

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
    print("Hello World!")
