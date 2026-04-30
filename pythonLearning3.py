import json
import os

movies = []

def loadMovies():
    global movies
    try:
        with open("movies.json", "r") as f:
            movies = json.load(f)
    except FileNotFoundError:
        movies = []

def saveMovies():
    with open("movies.json", "w") as f:
        json.dump(movies, f)

def addMovie(title, release_date):
    moviedict = {"title" : title, "release_date" : release_date}
    movies.append(moviedict)
    print(f"Successfully added {moviedict['title']}.")
    saveMovies()

def removeMovie(title):
    for movie in movies:
        if movie["title"] == title:
            print(f"Removing {movie['title']} from list...")
            movies.remove(movie)
            saveMovies()
            return
        
def getMovie(title):
    for movie in movies:
        if movie["title"] == title:
            print(f"Title: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            return 
    print(f"Sorry, {title} was not found!")

def listMovie():
    for movie in movies:
        print(f"{movie['title']} : {movie['release_date']}")

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    loadMovies()
    clearScreen()
    crudMenu = input("What would you like to do?" \
    "\n1. Add a movie\n2. Remove a movie" \
    "\n3. Get a movie\n4. List all movies\nQ. Quit\n")
    if crudMenu == "1":
        addMovieTitle = input("Name of movie to add to database: ")
        addMovieReleaseDate = input(f"Release date of {addMovieTitle}: ")
        addMovie(addMovieTitle, addMovieReleaseDate)
        input("")
    elif crudMenu == "2":
        removeMovieTitle = input("Name of movie to remove: ")
        removeMovie(removeMovieTitle)
        input("")
    elif crudMenu == "3":
        getMovieTitle = input("Name of movie to find in database: ")
        getMovie(getMovieTitle)
        input("")
    elif crudMenu == "4":
        listMovie()
        input("")
    elif crudMenu == "Q" or crudMenu == "q":
        break