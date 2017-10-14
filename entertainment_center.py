import fresh_tomatoes
import media

#define your list of movies here
#order of inputs: title, imdb link, poster link, trailer link
beauty_beast = media.Movie("Beauty and The Beast","http://www.imdb.com/title/tt2771200/","https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg","https://www.youtube.com/watch?v=OvW_L8sTu5E")
jungle_book = media.Movie("The Jungle Book","http://www.imdb.com/title/tt3040964/","https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg","https://www.youtube.com/watch?v=C4qgAaxB_pc&t=9s")
frozen = media.Movie("Frozen","http://www.imdb.com/title/tt2294629/?ref_=nv_sr_1","https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg","https://www.youtube.com/watch?v=R-cdIvgBCWY")
brave = media.Movie("Brave","http://www.imdb.com/title/tt1217209/?ref_=nv_sr_3","https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg","https://www.youtube.com/watch?v=TEHWDA_6e3M")
maleficent = media.Movie("Maleficent","http://www.imdb.com/title/tt1587310/?ref_=nv_sr_1","https://upload.wikimedia.org/wikipedia/en/5/55/Maleficent_poster.jpg","https://www.youtube.com/watch?v=w-XO4XiRop0")
cinderella = media.Movie("Cinderella","http://www.imdb.com/title/tt1661199/?ref_=nv_sr_1","https://upload.wikimedia.org/wikipedia/en/c/c2/Cinderella_2015_official_poster.jpg","https://www.youtube.com/watch?v=20DF6U1HcGQ")

#list of movies to be displayed
movies = [beauty_beast, cinderella, jungle_book, maleficent, frozen, brave]
fresh_tomatoes.open_movies_page(movies)
