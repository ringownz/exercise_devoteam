from starlette import status

from src.services import episodeService
from fastapi import APIRouter

router = APIRouter()


@router.get("/", status_code=status.HTTP_201_CREATED)
async def get_episodes():
    # Get all episodes from API
    return episodeService.get_episodes()


@router.get("/filter/", status_code=status.HTTP_200_OK)
async def filter_episodes(season: int = None):
    # Get all episodes from API
    return episodeService.filter_episodes_by_rating(season)


@router.get("/{episode_id}", status_code=status.HTTP_200_OK)
async def get_episode(episode_id: str):
    # Return information about episode id in a list
    return episodeService.get_episode_info(episode_id)
