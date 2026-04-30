import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

def searchMovie(query):
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": query
    }
    response = requests.get(url, params=params)
    data = response.json()
    for i, movie in enumerate(data["results"][:5]):
        print(f"{i+1}. {movie['title']} - {movie['release_date']}")