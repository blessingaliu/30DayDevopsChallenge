import requests
import boto3
import json

# Initialize AWS SDK clients
s3_client = boto3.client('s3')
secrets_manager_client = boto3.client('secretsmanager')

# AWS S3 Setup
S3_BUCKET_NAME = "movie-recommendations-bucket"  # Replace with your S3 bucket name

# Function to fetch the TMDb API Key from AWS Secrets Manager
def fetch_tmdb_api_key():
    """Retrieve the TMDb API key from AWS Secrets Manager."""
    secret_name = "TMDb_API_Key"  # Replace with the name of your secret in Secrets Manager

    try:
        # Retrieve the secret value from Secrets Manager
        response = secrets_manager_client.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        secret_dict = json.loads(secret)
        return secret_dict.get("TMDB_API_KEY")  # Assuming your secret is stored with this key
    except Exception as e:
        print(f"Error fetching secret from AWS Secrets Manager: {e}")
        return None

# Retrieve the TMDb API key securely
TMDB_API_KEY = fetch_tmdb_api_key()
if not TMDB_API_KEY:
    print("Error: Unable to fetch TMDb API key from Secrets Manager.")
    exit(1)

BASE_URL = "https://api.themoviedb.org/3"

def upload_to_s3(file_name, data, folder_name):
    """Upload data to S3."""
    try:
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=f"{folder_name}/{file_name}",
            Body=json.dumps(data)
        )
        print(f"Data uploaded successfully to S3://{S3_BUCKET_NAME}/{folder_name}/{file_name}")
    except Exception as e:
        print(f"Error uploading data to S3: {e}")

def fetch_genres():
    """Fetch a list of movie genres from TMDb."""
    url = f"{BASE_URL}/genre/movie/list"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        genres = response.json()["genres"]
        print("\nAvailable Genres:")
        for genre in genres:
            print(f"{genre['id']}: {genre['name']}")
        # Upload genres data to S3
        upload_to_s3("genres.json", genres, "raw/genres")
        return genres
    except requests.exceptions.RequestException as e:
        print(f"Error fetching genres: {e}")
        return []

def fetch_popular_movies():
    """Fetch a list of popular movies from TMDb."""
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "page": 1  # Fetch the first page of results
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        movies = response.json()["results"]
        print("\nAvailable Popular Movies and their IDs:")
        for movie in movies:
            print(f"{movie['id']}: {movie['title']} (Rating: {movie['vote_average']})")
        # Upload movies data to S3
        upload_to_s3("popular_movies.json", movies, "raw/movies")
        return movies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching popular movies: {e}")
        return []

def fetch_movie_details(movie_id):
    """Fetch details of a specific movie by its ID."""
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        movie_details = response.json()
        print(f"\nMovie Details for '{movie_details['title']}':")
        print(f"Release Date: {movie_details['release_date']}")
        print(f"Rating: {movie_details['vote_average']}")
        print(f"Overview: {movie_details['overview']}")
        # Upload movie details to S3
        upload_to_s3(f"movie_{movie_id}_details.json", movie_details, "raw/movies")
        return movie_details
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie details: {e}")
        return {}

def fetch_recommendations(movie_id):
    """Fetch recommendations for a specific movie by its ID."""
    url = f"{BASE_URL}/movie/{movie_id}/recommendations"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "page": 1
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        recommendations = response.json()["results"]
        print(f"\nRecommendations for Movie ID {movie_id}:")
        for movie in recommendations:
            print(f"{movie['title']} (Rating: {movie['vote_average']})")
        # Upload recommendations to S3
        upload_to_s3(f"movie_{movie_id}_recommendations.json", recommendations, "raw/recommendations")
        return recommendations
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recommendations: {e}")
        return []

def main():
    print("Welcome to the Movie Recommendation System!")
    while True:
        print("\nChoose an option:")
        print("1. Fetch Genres")
        print("2. Fetch Movie Details")
        print("3. Fetch Recommendations")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            fetch_genres()
        elif choice == "2":
            print("\nFetching Popular Movies...")
            movies = fetch_popular_movies()  # Show popular movies first
            if movies:
                movie_id = input("\nEnter the Movie ID for details: ").strip()
                if movie_id.isdigit():
                    fetch_movie_details(int(movie_id))
                else:
                    print("Invalid input. Please enter a valid Movie ID.")
        elif choice == "3":
            print("\nFetching Popular Movies...")
            movies = fetch_popular_movies()  # Show popular movies first
            if movies:
                movie_id = input("\nEnter the Movie ID for recommendations: ").strip()
                if movie_id.isdigit():
                    fetch_recommendations(int(movie_id))
                else:
                    print("Invalid input. Please enter a valid Movie ID.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
