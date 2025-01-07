
---

## **How to set up environment to complete the Weather Dashboard**

This guide explains how to create a weather dashboard app that fetches weather data from OpenWeather API and uploads it to an AWS S3 bucket with public access for the JSON files.

---

### **1. Prerequisites**

Before setting up the environment, complete the following steps:

---

#### **1.1 Create an AWS Account (if you don’t already have one)**

1. **Go to [AWS Free Tier Signup](https://aws.amazon.com/free/).**
   - Click **"Create a Free Account"**.
2. **Enter Your Details:**
   - Provide an email address, password, and account name.
3. **Select the Account Type:**
   - Choose **"Personal"** or **"Professional"**.
4. **Billing Information:**
   - Enter your credit/debit card details for verification.
5. **Verify Your Identity:**
   - Provide your phone number and complete the phone verification.
6. **Choose a Support Plan:**
   - Select **"Basic Support (Free)"** unless you need additional support.
7. **Complete Registration:**
   - Wait for the confirmation email that your account is active.

---

#### **1.2 Obtain OpenWeather API Key**

1. Visit [OpenWeather API](https://openweathermap.org/api).
2. Sign up for a free account if you don’t have one.
3. Once logged in:
   - Navigate to **API Keys** in your account dashboard.
   - Generate and copy your API key.

---

#### **1.3 Install Required Tools**

Ensure the following tools are installed:
- **Python 3.x**: [Download](https://www.python.org/downloads/).
- **pip**: Bundled with Python. Verify installation:
  ```bash
  python3 -m pip --version
  ```
- **AWS CLI**: [Download](https://aws.amazon.com/cli/). Verify installation:
  ```bash
  aws --version
  ```
- **VS Code**: [Download](https://code.visualstudio.com/).
  - Install the **Python extension** from the Extensions Marketplace.

---

### **2. Log in to AWS CLI**

Log in using the AWS CLI:

```bash
aws configure
```

- Enter your **AWS Access Key ID** and **AWS Secret Access Key** (generated earlier).
- Enter your default region (e.g., `us-west-2`).
- Set the output format to `json`.

---

### **3. Create an S3 Bucket**

Create a new S3 bucket to store the JSON files:

```bash
aws s3api create-bucket --bucket your-bucket-name --region your-region --create-bucket-configuration LocationConstraint=your-region
```

- Replace `your-bucket-name` with your desired bucket name.
- Replace `your-region` with your AWS region (e.g., `us-west-2`).

---

### **4. Set Bucket Policy for Public Access**

Update the bucket policy to make the JSON files publicly accessible:

1. **Edit Bucket Policy**:

   Create a JSON policy file named `bucket-policy.json`:

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

   Replace `your-bucket-name` with your S3 bucket name.

2. **Apply the Policy**:

   Run the following command to apply the policy:

   ```bash
   aws s3api put-bucket-policy --bucket your-bucket-name --policy file://bucket-policy.json
   ```

3. **Enable Static Website Hosting (Optional)**:

   If you want to access JSON files via a static website, enable static website hosting:

   ```bash
   aws s3 website s3://your-bucket-name/ --index-document index.html --error-document error.html
   ```

---

### **5. Set Up Project Directory**

Set up the project structure and create necessary files:

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

### **6. Install Dependencies**

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   ```

2. Add and install required libraries:

   ```bash
   echo "boto3==1.26.137" >> requirements.txt
   echo "python-dotenv==1.0.0" >> requirements.txt
   echo "requests==2.28.2" >> requirements.txt
   pip install -r requirements.txt
   ```

---

### **7. Add Environment Variables**

Store sensitive data in a `.env` file:

```bash
echo "OPENWEATHER_API_KEY=your_openweather_api_key" >> .env
echo "AWS_BUCKET_NAME=your-bucket-name" >> .env
```

Replace placeholders with:
- **`your_openweather_api_key`**: Your OpenWeather API key.
- **`your-bucket-name`**: Name of your S3 bucket.

---

### **8. Write the Weather Dashboard Script**

Implement the functionality in `src/weather_dashboard.py`:

```python
import boto3
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
```

---

### **9. Run the Application**

Run the script to test functionality:

```bash
python3 src/weather_dashboard.py
```

You can now access the JSON file using the S3 public URL:

```bash
https://your-bucket-name.s3.your-region.amazonaws.com/city_weather.json
```
