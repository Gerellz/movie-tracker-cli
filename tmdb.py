import requests
import os
from dotenv import load_dotenv

# reads the env file and loads contents for os.getenv
load_dotenv()

# stores the api key from the env file into a usable variable
API_KEY = os.getenv("TMDB_API_KEY")

# method to query the database and return a list of movies that the user might be referencing
def searchMovie(query):
    # takes the url and appends the api key and the query subject
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": query
    }
    # sends a get request to the url with the parameters
    try:
        response = requests.get(url, params=params)
    except requests.exceptions.ConnectionError:
        print("Uh-oh. Looks like you're not connected!")
        return None
    # receives a response and stores that json into a variable, data
    data = response.json()
    # loops through the data and returns an indexed page of results related to the query
    for i, movie in enumerate(data["results"][:5]):
        print(f"{i+1}. {movie['title']} - {movie['release_date']}")
    try:
        choice = int(input("Select a movie from the list by number: "))
        if choice < 1 or choice > 5:
            print("Error. Please select a movie from list.")
            return None
    except ValueError:
        print("Error. Please enter a valid selection.")
        return None
    selected = data["results"][choice - 1]
    return selected