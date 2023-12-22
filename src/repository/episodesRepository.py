from src.model import Episode
from src import db_context


def save(episode: Episode):
    sql = ''' INSERT INTO episodes(imdb_id, title, released, episode, season, imdb_rating)
                    VALUES(?,?,?,?,?,?) '''

    db_context.cur.execute(sql, (
    episode.imdb_id, episode.title, episode.released, episode.episode, episode.season, episode.imdb_rating))
    db_context.cur.connection.commit()


def find_episode(episode_id):
    sql = ''' select *
            from episodes
            where imdb_id = (?)
            '''
    cur = db_context.con.cursor()
    data = cur.execute(sql, episode_id)
    row = data.fetchone()
    return row
    # db_context.cur.connection.commit()
    # return data


def create_episode(episode: Episode):
    connection = db_context.create_connection("database.db")
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO episodes(imdb_id, title, released, episode, season, imdb_rating)
                    VALUES(?,?,?,?,?,?)''', (
    episode.imdb_id, episode.title, episode.released, episode.episode, episode.season, episode.imdb_rating))
    connection.commit()
    connection.close()


def get_episode(episode_id: str):
    connection = db_context.create_connection("database.db")
    cursor = connection.cursor()
    cursor.execute('''SELECT imdb_id,* FROM episodes
                    WHERE imdb_id = ?''', (episode_id,))
    row = cursor.fetchone()
    connection.commit()
    connection.close()
    return row


def get_all_episodes():
    connection = db_context.create_connection("database.db")
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM episodes ORDER BY season, episode''')
    all = cursor.fetchall()
    connection.commit()
    connection.close()
    return all
