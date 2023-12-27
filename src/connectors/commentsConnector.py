from fastapi import APIRouter
from starlette import status

from src.services import commentService

router = APIRouter()


@router.post("/{episode_id}", status_code=status.HTTP_201_CREATED)
async def create_comment(episode_id: str, comment: str):
    response = commentService.create_comment(episode_id, comment)
    if response is not None:
        if type(response) == Exception:
            return response.__str__()
        return f"Comment added with id: {response}"


@router.get("/{comment_id}", status_code=status.HTTP_200_OK)
async def get_comment(comment_id: int):
    return commentService.get_comment(comment_id)


@router.get("/all/{episode_id}", status_code=status.HTTP_200_OK)
async def get_all_comments(episode_id: str = None):
    # Return information about episode id in a list
    return commentService.get_all_comments(episode_id)


@router.post("/id/{comment_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_comment(comment_id: int, episode_id: str, comment: str):
    return commentService.update_comment(comment_id, episode_id, comment)


@router.delete("/id/{comment_id}", status_code=status.HTTP_200_OK)
async def delete_comment(comment_id: int):
    response = commentService.delete_comment(comment_id)
    if response is None:
        return f"Comment with id {comment_id} deleted successfully"
