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
        result = validate_episode(episode_id)
        if type(result) is Exception:
            return result

        comment = Comment(episode_id, comment)  # Validar dados de dominio
        return commentRepository.create_comment(comment)
    except Exception as e:
        return e


def get_all_comments(episode_id):
    result = validate_episode(episode_id)
    if type(result) is Exception:
        return result.__str__()
    listOfComments = []
    all_from_db = commentRepository.get_all_comments(episode_id)
    for each in all_from_db:
        listOfComments.append(mapper.show_user_all_comment_from_db(each))

    return mapper.show_user_list_comments(episode_id, listOfComments)


def get_comment(comment_id):
    row = commentRepository.get_comment_by_id(comment_id)
    if row is None:
        return f"Comment with id {comment_id} does not exist"
    data_to_user = mapper.show_comment_to_user_from_db_by_id(row)
    return data_to_user


def update_comment(comment_id, episode_id, comment):
    try:
        result = validate_episode(episode_id)
        if type(result) is Exception:
            return result.__str__()

        row_updated = commentRepository.update_comment(comment_id, episode_id, comment)
        if row_updated is None:
            return f"Couldn't update comment with id {comment_id}"
        return mapper.show_comment_to_user_from_db_by_id(row_updated)
    except Exception as e:
        return e


def delete_comment(comment_id):
    result = commentRepository.delete_comment(comment_id)
    #if result is None or result == 0:
    #    return f"Could not delete comment with id {comment_id}"
    #return f"Comment with id: {comment_id} deleted"
    return "Operation Completed."
