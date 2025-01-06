import os
import json
import boto3
import requests
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        # Initialize environment variables
        self.aws_bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.aws_region = os.getenv("AWS_REGION")
        self.openweather_api_key = os.getenv("OPENWEATHER_API_KEY")

        # Initialize AWS S3 client using the default credential provider (AWS CLI credentials)
        self.s3_client = boto3.client("s3", region_name=self.aws_region)

    def create_bucket_if_not_exists(self):
        """
        Create the S3 bucket if it does not exist.
        """
        try:
            # Check if bucket exists
            self.s3_client.head_bucket(Bucket=self.aws_bucket_name)
            print(f"Bucket '{self.aws_bucket_name}' already exists.")
        except ClientError as e:
            # If bucket does not exist, create it
            if e.response['Error']['Code'] == '404':
                print(f"Bucket '{self.aws_bucket_name}' does not exist. Creating...")
                self.s3_client.create_bucket(
                    Bucket=self.aws_bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': self.aws_region}
                )
                print(f"Bucket '{self.aws_bucket_name}' created successfully.")
            else:
                raise

    def fetch_weather(self, city):
        """
        Fetch weather data for the specified city from OpenWeatherMap API.
        """
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.openweather_api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            print(f"Weather data fetched for city: {city}")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch weather data: {e}")
            return None

    def save_to_s3(self, data, city):
        """
        Save weather data to the S3 bucket.
        Args:
            data (dict): The weather data to save.
            city (str): The city name, used in the file name.
        """
        file_name = f"{city.lower()}_weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            self.s3_client.put_object(
                Bucket=self.aws_bucket_name,
                Key=file_name,
                Body=json.dumps(data),
                ContentType="application/json",
            )
            print(f"Weather data for {city} saved to S3 as '{file_name}'.")
        except ClientError as e:
            print(f"Failed to upload weather data to S3: {e}")

    def run(self, city):
        """
        Run the full process: initialize, fetch weather, and save to S3.
        """
        print("Initializing Weather Dashboard...")
        self.create_bucket_if_not_exists()
        weather_data = self.fetch_weather(city)
        if weather_data:
            self.save_to_s3(weather_data, city)

# Example usage
if __name__ == "__main__":
    city_name = input("Enter the city name: ").strip()
    dashboard = WeatherDashboard()
    dashboard.run(city_name)
