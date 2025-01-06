
---

# 🌤️ AWS Weather Dashboard Application

This application fetches **weather data** from the **OpenWeather** API and displays it on a dashboard. It uses **AWS** services such as **S3** for data storage and **AWS CLI** for managing AWS resources. The app is built with **Python** and integrates with **AWS Cloud** for deployment. 

You can run the app locally or inside a Docker container.

---

## 🛠️ Prerequisites

Before you run the application, you’ll need the following:

- 🐍 **Python 3.x** or **Docker** installed on your local machine.
- 🛠️ **AWS CLI** installed and configured with your AWS credentials.
- 🌍 **OpenWeather API Key** (for fetching weather data).
- ☁️ **AWS Account** with access to services like **S3**.

---

## 🚀 Setup

### 1. Clone the repository:

```bash
git clone <repository_url>
cd Day1-WeatherDashboard
```

### 2. Create required directories and files:

```bash
mkdir src tests data
touch src/__init__.py src/weather_dashboard.py
touch requirements.txt README.md .env
echo ".env" >> .gitignore
echo "pycache/" >> .gitignore
echo ".zip" >> .gitignore
```

### 3. Install dependencies:

Create the `requirements.txt` file and add the following dependencies:

```txt
boto3===1.26.137
python-dotenv==1.0.0
requests==2.28.2
```

Install the requirements:

```bash
pip install -r requirements.txt
```

### 4. 🛠️ AWS Configuration:

Configure your AWS CLI by running:

```bash
aws configure
```

This will prompt you for:

- AWS Access Key ID
- AWS Secret Access Key
- Default region name
- Default output format (optional)

These credentials will be used by `boto3` to interact with AWS services like **S3**.

### 5. Add environment variables:

Create a `.env` file in the project root directory and add your **OpenWeather API key** and **AWS Bucket name**:

```txt
OPENWEATHER_API_KEY=your_api_key_here
AWS_BUCKET_NAME=your_bucket_name_here
```

---

## 💻 Running the Application

### Option 1: Running Locally

1. Set up a Python virtual environment:

```bash
python3 -m venv weather-dash-env
source weather-dash-env/bin/activate  # On Windows: weather-dash-env\Scripts\activate
```

2. Reinstall dependencies inside the virtual environment:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python3 src/weather_dashboard.py
```

This will:

- Fetch weather data from the **OpenWeather API**.
- Upload the data to your **AWS S3 bucket**.
- Display the weather data in the dashboard.

---

### Option 2: Running with Docker

1. **Build the Docker image**:

```bash
docker build -t weather-dashboard .
```

2. **Run the container** with environment variables from the `.env` file:

```bash
docker run --env-file .env weather-dashboard
```

This will start the container and run the application, using the environment variables in your `.env` file for configuration.

---

## 🌐 AWS Configuration

The app uses AWS credentials stored locally via the **AWS CLI** configuration (`~/.aws/credentials`). These credentials enable the app to interact with AWS services like **S3**. The credentials are necessary for uploading data to the **S3 bucket** defined in your `.env` file.

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---