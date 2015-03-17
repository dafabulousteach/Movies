import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that come to life", 
	"http://cdnvideo.dolimg.com/cdn_assets/5670999ffe25e4bd664bc9486adef5171a494e7f.jpg", 
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
	"A substitute teacher rocks a school",
	"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=XCwy6lW5Ixc")

goodfellas = media.Movie("Goodfellas",
	"A true story of life in the mob",
	"http://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
	"https://www.youtube.com/watch?v=qo5jJpHtI1Y")

hunger_games = media.Movie("Hunger Games",
	"A girl takes on a brutal empire, and inspires a revolution",
	"http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
	"https://www.youtube.com/watch?v=mfmrPu43DF8")

ratatouille = media.Movie("Ratatouille",
	"A rat becomes a chef",
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=niD-jahFURU")

movies = [toy_story, avatar, school_of_rock, goodfellas, hunger_games, ratatouille]
fresh_tomatoes.open_movies_page(movies)


