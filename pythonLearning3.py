import json
import os
import tmdb

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
        json.dump(movies, f, indent=4)

def addMovie(title, release_date, description):
    moviedict = {"title" : title, "release_date" : release_date, "description" : description}
    for movie in movies:
        if movie["title"].lower() == title.lower():
            print(f"{movie['title']} is already in the database!")
            return
    movies.append(moviedict)
    print(f"Successfully added {moviedict['title']}.")
    saveMovies()

def removeMovie(title):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            print(f"Removing {movie['title']} from list...")
            movies.remove(movie)
            saveMovies()
            return
        else:
            print("Sorry, that movie was not found. Maybe you misspelled it?")
        
def getMovie(title):
    found = False
    for movie in movies:
        if title.lower() in (movie["title"]).lower():
            print(f"Title: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            print(f"Description: {movie['description']}")
            found = True
    if not found:
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
        searchMovieTitle = input("What are you looking for? ")
        returnedMovie = tmdb.searchMovie(searchMovieTitle)
        if returnedMovie is not None:
            addMovie(returnedMovie["title"], returnedMovie["release_date"], returnedMovie["overview"])
            input("Can't wait to see it! Press any key to continue.")
    elif crudMenu == "2":
        listMovie()
        removeMovieTitle = input("Name of movie to remove: ")
        removeMovie(removeMovieTitle)
        input("Yeah, I never liked that one either. Press any key to continue.")
    elif crudMenu == "3":
        getMovieTitle = input("Name of movie to find in database: ")
        getMovie(getMovieTitle)
        input("Oh, that's a good one! Press any key to continue.")
    elif crudMenu == "4":
        listMovie()
        input("Find anything you like? Press any key to continue.")
    elif crudMenu == "Q" or crudMenu == "q":
        print("Goodbye.")
        break