import webbrowser


class Movie():
        """A class for movies.
        A movie should have a title, IMDb URL, poster image URL,
        and trailer URL."""

        def __init__(self, movie_title, movie_page,
                     movie_poster, movie_trailer):
                self.title = movie_title
                self.imdb_link = movie_page
                self.poster_image_url = movie_poster
                self.trailer_youtube_url = movie_trailer

        def show_trailer(self):
                """Plays the movie trailer in a new browser window."""
                webbrowser.open(self.trailer_youtube_url)
