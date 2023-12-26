def show_user_from_db_by_id(row_db):

    if len(row_db) == 6:
        imdb_id, title, released, episode, season, imdb_rating = row_db
    elif len(row_db) == 7: #Find by ID returns everything + id
        _,imdb_id,title,released,episode,season,imdb_rating = row_db

    return {
        'imdb_id': imdb_id,
        'title': title,
        #'released': released,
        'season': season,
        'episode': episode,
        'imdb_rating': imdb_rating
    }


def show_user_all_comment_from_db(row_db):
    id, _, comment = row_db

    return {
        'id': id,
        'comment': comment
    }


def show_user_list_comments(episode_id, listOfComments):
    if episode_id is not None:
        return {
            'episode': episode_id,
            'list_all_comments': listOfComments
        }
    else:
        return {
            'list_comments': listOfComments
        }


def show_comment_to_user_from_db_by_id(row):
    _, comment_id, episode_id, comment = row

    return {
        'id': comment_id,
        'episode_id': episode_id,
        'comment': comment
    }
