import requests
import boto3
import json
import os

# Initialize S3 client
s3_client = boto3.client('s3')
bucket_name = 'movie-insight-bucket'  # Use your S3 bucket name

# Fetch TMDb API Key from Lambda Environment Variables (or Secrets Manager)
TMDB_API_KEY = os.environ['TMDB_API_KEY']  # Set this in Lambda environment variables
BASE_URL = "https://api.themoviedb.org/3"

# Lambda function to fetch data from TMDb API and store it in S3
def lambda_handler():
    # Fetch genres from TMDb API
    genres = fetch_genres()
    # Fetch popular movies from TMDb API
    movies = fetch_popular_movies()

    # Store both in S3
    if genres:
        upload_to_s3("genres.json", genres, "raw/genres")
    if movies:
        upload_to_s3("popular_movies.json", movies, "raw/movies")

    return {
        'statusCode': 200,
        'body': json.dumps('Data fetched and stored successfully!')
    }

def fetch_genres():
    """Fetch a list of movie genres from TMDb."""
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": TMDB_API_KEY, "language": "en-US"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        genres = response.json()["genres"]
        print(f"Fetched genres: {len(genres)}")
        return genres
    except requests.exceptions.RequestException as e:
        print(f"Error fetching genres: {e}")
        return []

def fetch_popular_movies():
    """Fetch a list of popular movies from TMDb."""
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": TMDB_API_KEY, "language": "en-US", "page": 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        movies = response.json()["results"]
        print(f"Fetched popular movies: {len(movies)}")
        return movies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching popular movies: {e}")
        return []

def upload_to_s3(file_name, data, folder_name):
    """Upload data to S3."""
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=f"{folder_name}/{file_name}",
            Body=json.dumps(data)
        )
        print(f"Data uploaded to S3://{bucket_name}/{folder_name}/{file_name}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

