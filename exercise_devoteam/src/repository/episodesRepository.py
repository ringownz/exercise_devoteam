from sqlite3 import IntegrityError

from src.model import Episode
from src import db_context


def create_episode(episode: Episode):
    connection = db_context.new_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('''INSERT INTO episodes(imdb_id, title, released, episode, season, imdb_rating)
                        VALUES(?,?,?,?,?,?)''', (
            episode.imdb_id, episode.title, episode.released, episode.episode, episode.season, episode.imdb_rating))
    except IntegrityError:
        print("UNIQUE KEY ALREADY EXISTS")
    finally:
        connection.commit()
        connection.close()


def get_episode_by_id(episode_id: str):
    connection = db_context.new_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT imdb_id,* FROM episodes
                    WHERE imdb_id = ?''', (episode_id,))
    row = cursor.fetchone()
    connection.commit()
    connection.close()
    return row


def get_all_episodes():
    connection = db_context.new_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM episodes ORDER BY season, episode''')
    all = cursor.fetchall()
    connection.commit()
    connection.close()
    return all


def get_episodes_by_rating(season):
    # Filter by season and rating > 8.8
    connection = db_context.new_connection()
    cursor = connection.cursor()

    sql = '''SELECT * FROM episodes WHERE imdb_rating > 8.8'''
    if season is not None:
        cursor.execute(sql + " AND season = ?", (season,))
    else:
        cursor.execute(sql)
    all = cursor.fetchall()
    connection.commit()
    connection.close()
    return all
