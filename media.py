class Movie(object):

    def __init__(self, title, poster_image_url, trailer_youtube_url, rating):
        """Constructor for the Movie object. Takes in a title, the URL for a
        poster image, a URL for the youtube trailer, and a personal rating for
        that movie."""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        if rating < 1 or rating > 5:
            raise ValueError("""Personal ratings must be between 1 and 5 where
                1 is your least favorite and 5 is your all time favorite.""")
        self.rating = rating

    def __lt__(self, other):
        """Determines if the instance's rating is less than another
        instance."""
        return self.rating < other.rating

    def __gt__(self, other):
        """Determines if the instance's rating is greater than another
            instance."""
        return self.rating > other.rating

    def __repr__(self):
        """displays the title of the movie when the object is displayed to the
        screen"""
        return self.title
