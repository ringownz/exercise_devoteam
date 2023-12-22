import os
import sqlite3


# Database context
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except ConnectionError as e:
        print(e)

    return conn


#os.remove("database.db")
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS episodes
(imdb_id text PRIMARY KEY, title text, released text, episode integer, season integer, imdb_rating float)''')


def create_episodes():
    connection = create_connection("database.db")
    cursor = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS episodes
    (imdb_id text PRIMARY KEY, title text, released text, episode integer, season integer, imdb_rating float)''')
    connection.commit()
    connection.close()


def create_all():
    create_episodes()


#
# https://stackoverflow.com/questions/67056605/how-to-drop-all-tables-in-sqlite3-using-python
#
TABLE_PARAMETER = "{TABLE_PARAMETER}"
DROP_TABLE_SQL = f"DROP TABLE {TABLE_PARAMETER};"
GET_TABLES_SQL = "SELECT name FROM sqlite_schema WHERE type='table';"

def delete_all_tables():
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
