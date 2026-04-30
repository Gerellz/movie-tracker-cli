class Movie():
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def describe(self):
        print(f"{self.title} released on {self.release_date}")

movie = Movie("The Matrix", "03-31-99")
movie.describe()

movies = ["Shawshank Redemption", "Star Wars", "Space Jam"]
movie_years = {"Shawshank Redemption" : 1994, "Star Wars" : 1977, "Space Jam" : 1996}
print(f"The movie: {movies[0]} came out in {movie_years[movies[0]]}")

movies.append("Empire Strikes Back")
movie_years["The Matrix"] = 1999
for movie, year in movie_years.items():
    print(f"{movie} : {year}")