from ..model.Comment import Comment
from ..repository import episodesRepository, commentRepository
from ..utils import mapper


def validate_episode(episode_id):
    # Validate episode_id
    try:
        ep = episodesRepository.get_episode_by_id(episode_id)  # Validar injection chars ...
        if ep is None:
            raise Exception(f"Episode id {episode_id} does not exist")
    except Exception as e:
        return e


def create_comment(episode_id, comment):
    try:
        validate_episode(episode_id)

        comment = Comment(episode_id, comment)  # Validar dados de dominio
        commentRepository.create_comment(comment)
    except Exception as e:
        return e

def get_all_comments(episode_id):
    validate_episode(episode_id)

    listOfComments = []
    all_from_db = commentRepository.get_all_comments(episode_id)
    for each in all_from_db:
        listOfComments.append(mapper.show_user_all_comment_from_db(each))

    return mapper.show_user_list_comments(episode_id, listOfComments)


def get_comment(comment_id):
    row = commentRepository.get_comment_by_id(comment_id)
    data_to_user = mapper.show_comment_to_user_from_db_by_id(row)
    return data_to_user


def update_comment(comment_id, episode_id, comment):
    try:
        validate_episode(episode_id)

        return commentRepository.update_comment(comment_id, episode_id, comment)

    except Exception as e:
        return e


def delete_comment(comment_id):

    commentRepository.delete_comment(comment_id)
