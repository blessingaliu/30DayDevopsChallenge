
---

## How to Set Up Environment to Complete the Weather Dashboard

This guide walks you through the process of setting up a weather dashboard app that fetches weather data from the OpenWeather API and uploads it to an AWS S3 bucket for storing JSON files with public access.

## 1. Prerequisites: Account Setup & Tool Installation

### 1.1 Install Necessary Tools
- **Python 3.x**: Download Python from [here](https://www.python.org/downloads/). Once installed, verify the installation by running:
  ```bash
  python3 --version
  ```
  
- **pip**: Verify pip is installed with Python by running:
  ```bash
  pip --version
  ```

- **AWS CLI**: Download AWS CLI from [here](https://aws.amazon.com/cli/). After installation, verify it by running:
  ```bash
  aws --version
  ```

- **VS Code**: Download and install Visual Studio Code from [here](https://code.visualstudio.com/), and add the Python extension for enhanced development support.

---

### 1.2 Create an AWS Account & Access Keys

1. Go to the [AWS Free Tier Signup](https://aws.amazon.com/free/) page and create an AWS account.
2. After signing in, generate **Access Keys** for AWS CLI:
   - Navigate to the **IAM Console**.
   - In the left-hand menu, click **Users**, then select your user.
   - Under the **Security Credentials** tab, click **Create Access Key**.
   - Copy the **Access Key ID** and **Secret Access Key** and store them securely.

---

### 1.3 Obtain OpenWeather API Key

1. Visit the [OpenWeather API](https://openweathermap.org/api) page and sign up for a free account if you don’t have one.
2. Once logged in, navigate to **API Keys** and generate a new key. Copy the generated key.

---

## 2. Log in to AWS CLI

After setting up your AWS Access Keys, log in to the AWS CLI by running the following command:

```bash
aws configure
```

- Enter your **AWS Access Key ID** and **AWS Secret Access Key**.
- Set the **Default region** (e.g., `us-west-2`).
- Set the **Default output format** to `json`.

---

## 3. Create an S3 Bucket

1. Create a new S3 bucket to store the JSON files by running the following command:

```bash
aws s3api create-bucket --bucket your-bucket-name --region your-region --create-bucket-configuration LocationConstraint=your-region
```

Replace the placeholders with:
- `your-bucket-name`: The name you want for your S3 bucket.
- `your-region`: The AWS region of your bucket (e.g., `us-west-2`).

---

## 4. Set Bucket Policy for Public Access

1. Create a bucket policy to make the files publicly accessible by creating a file named `bucket-policy.json`:

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

2. Apply the policy to your S3 bucket:

```bash
aws s3api put-bucket-policy --bucket your-bucket-name --policy file://bucket-policy.json
```

---

## 5. Set Up Project Directory

1. Create the necessary project structure:

```bash
mkdir weather-dashboard
cd weather-dashboard
mkdir src tests data
touch src/__init__.py src/weather_dashboard.py
touch requirements.txt README.md .env
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore
```

---

## 6. Create a GitHub Account and Repository

1. **Sign Up for GitHub**: Visit [GitHub Signup](https://github.com/) and create an account.
2. **Create a Remote Repository**: Log in to GitHub, click **New Repository**, and give it a name (e.g., `weather-dashboard`).
3. **Push Local Repository to GitHub**:
   - Initialize a local Git repository:
     ```bash
     git init
     ```
   - Add and commit all files:
     ```bash
     git add .
     git commit -m "Initial commit"
     ```
   - Add the remote repository URL and push the changes:
     ```bash
     git remote add origin https://github.com/your-username/weather-dashboard.git
     git branch -M main
     git push -u origin main
     ```

---

## 7. Install Dependencies

1. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

2. Add dependencies to `requirements.txt`:

```bash
echo "boto3==1.26.137" >> requirements.txt
echo "python-dotenv==1.0.0" >> requirements.txt
echo "requests==2.28.2" >> requirements.txt
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 8. Add Environment Variables

1. Create a `.env` file in the root directory of your project and add the following lines:

```bash
OPENWEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME=your-bucket-name
```

Replace the placeholders with:
- **`your_openweather_api_key`**: Your OpenWeather API key.
- **`your-bucket-name`**: Name of your S3 bucket.

---

You are now ready to implement the Weather Dashboard Script in `src/weather_dashboard.py`. This includes fetching weather data from the OpenWeather API and uploading it to your S3 bucket.
