## Setting up local python env on VScode
- within the project directory
- mkdir src tests data
- touch src/__init__.py src/weather_dashboard.py
- touch requirements.txt README.md .env 
- echo ".env" >> .gitignore
- echo "__pycache__/" >> .gitignore
- echo ".zip" >> .gitignore
- echo "boto3===1.26.137" >> requirements.txt
- echo "python-dotenv==1.0.0" >> requirements.txt
- echo "requests==2.28.2" >> requirements.txt
- pip install -r requirements.txt
- aws config (access key, secret access key, region)
- echo "OPENWEATHER_API_KEY=your_api_key_here" >> .env
- echo "AWS_BUCKET_NAME=bucketname" >> .env 
- pip install python-dotenv


##### Create a new environment 
- python3 -m venv weather-dash-env
- source weather-dash-env/bin/activate (activate the environment)
- aws configure
- pip3 install -r requirements.txt
- pip install boto3 (using boto to use the aws cli access keys)
- python3 src/weather_dashboard.py
