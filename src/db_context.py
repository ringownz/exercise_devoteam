import os
import sqlite3

db = "database.db"


# Database context
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except ConnectionError as e:
        print(e)

    return conn


def new_connection():
    return create_connection(db)


def create_episodes():
    connection = new_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS episodes
    (imdb_id text PRIMARY KEY, title text, released text, episode integer, season integer, imdb_rating float)''')
    connection.commit()
    connection.close()


def create_comments():
    connection = new_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS comments
    (
    id integer UNIQUE PRIMARY KEY,
    episode_id text,
    comment text,
    FOREIGN KEY(episode_id) REFERENCES episodes(imdb_id)
    )
    ''')
    connection.commit()
    connection.close()


def create_all():
    print("Creating all tables...\n\n...\n..\n.")
    create_episodes()
    create_comments()


#
# https://stackoverflow.com/questions/67056605/how-to-drop-all-tables-in-sqlite3-using-python
#
TABLE_PARAMETER = "{TABLE_PARAMETER}"
DROP_TABLE_SQL = f"DROP TABLE {TABLE_PARAMETER};"
GET_TABLES_SQL = "SELECT name FROM sqlite_schema WHERE type='table';"


def delete_all_tables():
    con = new_connection()
    tables = get_tables(con)
    delete_tables(con, tables)


def get_tables(con):
    cur = con.cursor()
    cur.execute(GET_TABLES_SQL)
    tables = cur.fetchall()
    cur.close()
    return tables


def delete_tables(con, tables):
    cur = con.cursor()
    for table, in tables:
        sql = DROP_TABLE_SQL.replace(TABLE_PARAMETER, table)
        cur.execute(sql)
    cur.close()


def start():
    create_connection(db)
    delete_all_tables()
    create_all()
