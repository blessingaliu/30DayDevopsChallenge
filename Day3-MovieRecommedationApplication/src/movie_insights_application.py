import requests
import boto3
import json
import os

# initialize s3 client
s3_client = boto3.client('s3')
bucket_name = 'movie-insight-bucket'  # use your s3 bucket name

# fetch tmdb api key from lambda environment variables (or secrets manager)
TMDB_API_KEY = os.environ['TMDB_API_KEY']  # set this in lambda environment variables
BASE_URL = "https://api.themoviedb.org/3"

# lambda function to fetch data from tmdb api and store it in s3
def lambda_handler(event, context):  # added event and context parameters
    # fetch genres from tmdb api
    genres = fetch_genres()
    # fetch popular movies from tmdb api
    movies = fetch_popular_movies()

    # store both in s3
    if genres:
        upload_to_s3("genres.json", genres, "raw/genres")
    if movies:
        upload_to_s3("popular_movies.json", movies, "raw/movies")

    return {
        'statusCode': 200,
        'body': json.dumps('data fetched and stored successfully!')
    }

def fetch_genres():
    """fetch a list of movie genres from tmdb."""
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": TMDB_API_KEY, "language": "en-US"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        genres = response.json()["genres"]
        print(f"fetched genres: {len(genres)}")
        return genres
    except requests.exceptions.RequestException as e:
        print(f"error fetching genres: {e}")
        return []

def fetch_popular_movies():
    """fetch a list of popular movies from tmdb."""
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": TMDB_API_KEY, "language": "en-US", "page": 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        movies = response.json()["results"]
        print(f"fetched popular movies: {len(movies)}")
        return movies
    except requests.exceptions.RequestException as e:
        print(f"error fetching popular movies: {e}")
        return []

def upload_to_s3(file_name, data, folder_name):
    """upload data to s3."""
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=f"{folder_name}/{file_name}",
            Body=json.dumps(data)
        )
        print(f"data uploaded to s3://{bucket_name}/{folder_name}/{file_name}")
    except Exception as e:
        print(f"error uploading to s3: {e}")
