import webbrowser

#movie class definition
class Movie():
    def __init__(self, movie_title, movie_page, movie_poster, movie_trailer):
        self.title = movie_title
        self.imdb_link = movie_page
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
