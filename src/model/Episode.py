# create data model for episode
class Episode(object):
    imdb_id = str()
    title = str()
    released = str()
    season = int()
    episode = int()
    imdb_rating = float()

    def __init__(self, imdb_id, title, released, season, episode):
        self.imdb_id = imdb_id
        self.title = title
        self.released = released
        self.season = season
        self.episode = episode

    def set_rating(self, imdb_rating):
        self.imdb_rating = imdb_rating
