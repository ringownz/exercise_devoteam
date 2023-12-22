def show_user_from_db_by_id(row_db):

    if len(row_db) == 6:
        imdb_id, title, released, episode, season, imdb_rating = row_db
    elif len(row_db) == 7: #Find by ID returns everything + id
        _,imdb_id,title,released,episode,season,imdb_rating = row_db

    return {
        #'imdb_id': imdb_id,
        'title': title,
        #'released': released,
        'season': season,
        'episode': episode,
        'imdb_rating': imdb_rating
    }
