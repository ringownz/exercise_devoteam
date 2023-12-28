import uuid


class Comment(object):
    _id = str()
    episode_id = str()
    comment = str()

    def __init__(self, episode_id, comment):
        self.episode_id = episode_id
        self.comment = comment

    def insert_id(self, comment_id):
        self._id = comment_id
