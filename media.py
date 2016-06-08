class Movie():
    """This class provides a way to store movie related information."""  #  Used for __docs__ function

# Initializing our attributes for class Movie to be used in entertainment_center.py
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating, movie_duration, movie_release):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        self.duration = movie_duration
        self.release = movie_release
