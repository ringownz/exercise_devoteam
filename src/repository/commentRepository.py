from src.model import Comment
from src import db_context


def create_comment(comment: Comment):
    connection = db_context.new_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO comments(episode_id, comment)
                    VALUES(?,?)''', (
        comment.episode_id, comment.comment))
    connection.commit()
    connection.close()


def get_all_comments(episode_id=None):
    connection = db_context.new_connection()
    cursor = connection.cursor()
    sql = '''SELECT * FROM comments '''

    if episode_id is not None:
        cursor.execute(sql + '''WHERE episode_id = ? ''', (episode_id,))
    else:
        cursor.execute(sql)

    all = cursor.fetchall()
    connection.commit()
    connection.close()
    return all


def get_comment_by_id(comment_id):
    connection = db_context.new_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT id,* FROM comments
                    WHERE id = ?''', (comment_id,))
    row = cursor.fetchone()
    connection.commit()
    connection.close()
    return row


def update_comment(comment_id, episode_id, comment):
    connection = db_context.new_connection()
    cursor = connection.cursor()
    cursor.execute('''UPDATE comments
    SET episode_id = ?, comment = ? WHERE id = ?'''
                   , (episode_id, comment, comment_id,))
    row = cursor.fetchone()
    connection.commit()
    connection.close()
    return row


def delete_comment(comment_id):
    connection = db_context.new_connection()
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM comments
         WHERE id = ?'''
                   , (comment_id,))
    connection.commit()
    connection.close()
