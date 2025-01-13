### How to Set Up Environment to Complete the Weather Dashboard

This guide walks you through the process of setting up a weather dashboard app that fetches weather data from the OpenWeather API and uploads it to an AWS S3 bucket for storing JSON files with public access.

---

### 1. Prerequisites: Account Setup & Tool Installation

Before diving into building your Weather Dashboard app, you'll need to set up a few tools and accounts.

#### 1.1 Install Necessary Tools

To begin, make sure you have the following tools installed on your system:

- **Python 3.x**: Python is required to run the app locally.
  - [Download Python](https://www.python.org/downloads/).  
  - Once installed, verify the installation by running:
    ```bash
    python --version
    ```

- **pip**: Python's package manager that helps install dependencies.
  - Check if pip is installed with:
    ```bash
    pip --version
    ```

- **AWS CLI**: The AWS Command Line Interface (CLI) allows you to interact with AWS services directly from the command line.
  - [Download AWS CLI](https://aws.amazon.com/cli/).
  - Verify the installation by running:
    ```bash
    aws --version
    ```

- **VS Code**: This is an Integrated Development Environment (IDE) for writing your Python code.
  - Download and install [Visual Studio Code](https://code.visualstudio.com/).
  - For a better development experience, install the **Python extension** for VS Code.

---

#### 1.2 Create an AWS Account & Access Keys

To interact with AWS services like S3, you'll need an AWS account and access keys.

1. **Create an AWS Account**: 
   - Go to the [AWS Free Tier Signup](https://aws.amazon.com/free/) page and follow the prompts to create your account.
   
2. **Generate Access Keys for AWS CLI**:
   - After signing in to AWS, navigate to the **IAM Console**.
   - In the left menu, click **Users**, then select your username.
   - Under the **Security Credentials** tab, click **Create Access Key**.
   - Copy the **Access Key ID** and **Secret Access Key** and store them safely (you will need these in the next steps).

---

#### 1.3 Obtain OpenWeather API Key

To fetch weather data, you will need an API key from OpenWeather.

1. Visit the [OpenWeather API page](https://openweathermap.org/api).
2. Sign up for a free account if you don’t have one.
3. After logging in, go to **API Keys** and generate a new API key.
4. Copy the API key for use in the next steps.

---

### 2. Log in to AWS CLI

After setting up your AWS Access Keys, log in to the AWS CLI to authenticate and configure your environment.

1. Run the following command in your terminal:
   ```bash
   aws configure
   ```
2. Enter the **Access Key ID**, **Secret Access Key**, and the **Default region** (e.g., `us-west-2`).
3. Set the **Default output format** to `json`.

---

### 3. Create an S3 Bucket

Your weather data will be stored in an AWS S3 bucket. Here's how to create one.

1. To create a new S3 bucket, run this command (replace `your-bucket-name` and `your-region` with your chosen names):
   ```bash
   aws s3api create-bucket --bucket your-bucket-name --region your-region --create-bucket-configuration LocationConstraint=your-region
   ```

---

### 4. Set Bucket Policy for Public Access

You’ll need to make your bucket publicly accessible to allow reading the weather data files. 

1. Create a file named `bucket-policy.json` with the following content:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "PublicReadGetObject",
               "Effect": "Allow",
               "Principal": "*",
               "Action": "s3:GetObject",
               "Resource": "arn:aws:s3:::your-bucket-name/*"
           }
       ]
   }
   ```

   Replace `your-bucket-name` with your actual S3 bucket name.

2. Apply this policy to your S3 bucket by running:
   ```bash
   aws s3api put-bucket-policy --bucket your-bucket-name --policy file://bucket-policy.json
   ```

---

### 5. Set Up Project Directory

Now let’s set up the structure for your project:

1. Create the necessary project folders and files:

   ```bash
   mkdir weather-dashboard
   cd weather-dashboard
   mkdir src tests data
   touch src/__init__.py src/weather_dashboard.py
   touch requirements.txt README.md .env
   echo ".env" >> .gitignore
   echo "__pycache__/" >> .gitignore
   ```

   - **`src/`**: Directory for your Python scripts.
   - **`tests/`**: Directory for unit tests (if needed).
   - **`data/`**: Directory for storing your weather data files.
   - **`requirements.txt`**: This file will list your project dependencies.
   - **`.env`**: File to store environment variables such as API keys and AWS configurations.

---

### 6. Create a GitHub Account and Repository

To keep track of your code and collaborate with others, create a GitHub repository.

1. **Sign Up for GitHub**: If you don’t have an account, sign up at [GitHub Signup](https://github.com/).
2. **Create a New Repository**: Log in to GitHub, click **New Repository**, and name it (e.g., `weather-dashboard`).
3. **Push Your Code to GitHub**:
   - Initialize a local Git repository:
     ```bash
     git init
     ```
   - Add all files:
     ```bash
     git add .
     git commit -m "Initial commit"
     ```
   - Push the local repository to GitHub:
     ```bash
     git remote add origin https://github.com/your-username/weather-dashboard.git
     git branch -M main
     git push -u origin main
     ```

---

### 7. Install Dependencies

Now, install the necessary Python libraries for your project.

1. Create a virtual environment to isolate your dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   ```

2. Add the following dependencies to the `requirements.txt` file:

   ```
   boto3==1.26.137
   python-dotenv==1.0.0
   requests==2.28.2
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### 8. Add Environment Variables

The `.env` file is where you’ll store sensitive information such as your OpenWeather API key and AWS configurations.

1. Create a `.env` file in the root directory of your project.
2. Add the following lines, replacing placeholders with your actual information:

   ```bash
   OPENWEATHER_API_KEY=your_openweather_api_key
   AWS_BUCKET_NAME=your-bucket-name
   ```

---

Now that your environment is set up, you're ready to implement the Weather Dashboard Script in `src/weather_dashboard.py`. This script will fetch weather data from the OpenWeather API and upload it to your S3 bucket.
