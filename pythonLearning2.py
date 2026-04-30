movies = []

def addMovie(title, release_date):
    moviedict = {"title" : title, "release_date" : release_date}
    movies.append(moviedict)

addMovie("Star Wars", "1977")
addMovie("The Matrix", "1999")

for movie in movies:
    print(f"{movie["title"]} : {movie["release_date"]}")


def removeMovie(title):
    for movie in movies:
        if movie["title"] == title:
            print(f"Removing {movie["title"]} from list...")
            movies.remove(movie)
            return

removeMovie("Star Wars")

for movie in movies:
    print(f"{movie["title"]} : {movie["release_date"]}")

def getMovie(title):
    for movie in movies:
        if movie["title"] == title:
            print(f"Title: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            return 
    print(f"Sorry, {title} was not found!")

getMovie("Star Wars")