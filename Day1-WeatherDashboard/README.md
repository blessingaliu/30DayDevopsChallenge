# Setting up Local Python Environment on VS Code for Weather Dashboard 

This guide walks through setting up a local Python environment for a weather dashboard project that fetches weather data from OpenWeather API and stores it in an S3 bucket.

### Prerequisites

Ensure the following tools are installed on your system:
- Python 3.x
- pip (Python's package manager)
- AWS CLI (Command Line Interface)
- VS Code (with Python extension)

### 1. **Create Project Directory**

Within the project directory, create the necessary folders and files:

```bash
mkdir src tests data
touch src/__init__.py src/weather_dashboard.py
touch requirements.txt README.md .env
echo ".env" >> .gitignore
echo "pycache/" >> .gitignore
echo ".zip" >> .gitignore
```

- `src/`: Stores source code files.
- `tests/`: Directory for testing files.
- `data/`: Directory for storing fetched weather data.
- `.env`: Environment file for sensitive keys.
- `.gitignore`: Specifies files and directories to exclude from Git.
- `requirements.txt`: Stores project dependencies.

### 2. **Set up Dependencies**

Open `requirements.txt` and add the following libraries:

```bash
echo "boto3===1.26.137" >> requirements.txt
echo "python-dotenv==1.0.0" >> requirements.txt
echo "requests==2.28.2" >> requirements.txt
```

Now, install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. **Configure AWS CLI**

Run the AWS CLI configuration to set up your access keys and region:

```bash
aws configure
```

- Enter your AWS Access Key ID.
- Enter your AWS Secret Access Key.
- Enter your desired AWS region (e.g., `us-west-2`).

### 4. **Set up Environment Variables**

Create a `.env` file and add the following environment variables:

```bash
echo "OPENWEATHER_API_KEY=your_api_key_here" >> .env
echo "AWS_BUCKET_NAME=bucketname" >> .env
```

- Replace `your_api_key_here` with your OpenWeather API key.
- Replace `bucketname` with your S3 bucket name.

Ensure `.env` is added to `.gitignore` to keep it private.

### 5. **Create Python Virtual Environment**

Create and activate a virtual environment for the project:

```bash
python3 -m venv weather-dash-env
source weather-dash-env/bin/activate  # On macOS/Linux
```

This ensures your dependencies are installed in an isolated environment.

### 6. **Install Python Dependencies in Virtual Environment**

Once the virtual environment is activated, install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 7. **Install Additional Dependencies**

Install the `boto3` library to interact with AWS services:

```bash
pip install boto3
```

This will allow the project to interact with AWS services, such as S3.

### 8. **Run the Weather Dashboard Script**

Finally, you can run the Python script that fetches the weather data and uploads it to S3:

```bash
python3 src/weather_dashboard.py
```

This will execute the script and run the weather fetching process.
