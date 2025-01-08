## How to set up this Application 

This guide walks through setting up a local Python environment for the Game Day Alerts Lambda Application.

### Prerequisites

Ensure the following tools are installed on your system:
- Python 3.x
- pip (Python's package manager)
- AWS CLI (Command Line Interface)
- VS Code (with Python extension)

### 1. Step 1: Set Up SportsDataIO and Obtain the NBA API Key

- **Create a SportsDataIO Account**
    - Go to [SportsDataIO](https://sportsdata.io/) and sign up for an account.
    - Subscribe to the **NBA API Free Trial** to gain access.
    - Copy the API Key (example: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx) for use in the Lambda function.

---

### 2. Step 2: Manually Create an SNS Topic and Email Subscription

- **Create an SNS Topic**
    - Name the topic `gameday-topic` (or any other preferred name).
- **Create an SNS Subscription**
    - Set the **Protocol** to `Email`.
    - Enter the **Endpoint** as your email address (e.g., `emailaddress@example.com`).
- **Confirm the Subscription**
    - Go to your email inbox and find the confirmation email from AWS SNS.
    - Click the confirmation link to complete the subscription setup.

---

###  Step 3: Upload Lambda Code to S3 Bucket

#### Prepare Your Code

- Write the Python code for your Lambda function in a file called **[lambda_function.py](https://github.com/blessingaliu/30DayDevopsChallenge/blob/main/Day2-AWSGameDayNotificationService/src/lambda_function.py)**.

- After creating your code, **zip the file**:
```bash
zip lambda_code.zip lambda_function.py

```


#### Upload to S3

1. Go to the **S3 Console** in AWS Management Console.
2. **Select the Bucket** where you want to upload the Lambda code (or create a new one if needed).
3. **Click on "Upload"** and select your `lambda_code.zip` file.
4. **Note the Bucket Name** and **S3 URI Path** of the uploaded file. For example, it might be `my-bucket-name/path/to/lambda_code.zip`.

---

### Step 4: Prepare CloudFormation Template
- I named mine [game_day_notification.yaml](https://github.com/blessingaliu/30DayDevopsChallenge/blob/main/Day2-AWSGameDayNotificationService/src/game_day_notification.yaml)

**Key Considerations before deploying**
- Replace Placeholder values with the actual `SPORTS_API_KEY` and`SNS_TOPIC_ARN`.
- The `S3Bucket` should be `"youractuals3bucketname"` and the `S3Key` should be `"youractualS3URIPATH"`.

---
### Step 5: Deploy CloudFormation Stack

1. **Go to the CloudFormation Console**:
    - Open the **AWS Management Console** and navigate to **CloudFormation**.
    - Click on **Create Stack** → **With new resources (standard)**.
2. **Upload the CloudFormation Template Directly**:
    - **Select "Upload a template file"**.
    - Click on **Choose file** and select your updated CloudFormation template file (e.g., `game_day_notification.yaml`).
3. **Enter Stack Parameters** (not required for this application):
    - If your template asks for parameters (such as an email address for SNS), provide them during stack creation.
4. **Configure Stack Options** (not required for this application):
    - Specify stack name, tags, and permissions if needed.
5. **Review and Create**:
    - Review the template and parameters.
    - Click **Create Stack** to begin the deployment process.
  
---

### Step 6: Monitor Stack Creation

- **Track Progress**:
    - You can track the stack creation in the **Events** tab of the CloudFormation Console.
    - Ensure all resources (SNS Topic, Lambda Function, IAM Roles, EventBridge Rule) are created successfully
- **Check for Errors**:
    - If any resource fails to create, CloudFormation will show the error in the **Events** tab. Troubleshoot and correct any issues.

 
---
### Step 7: Test the Setup

1. **Manually Invoke Lambda (Optional)**:
    - In the **Lambda Console**, go to your Lambda function.
    - Click on **Test** and create a new test event. For example, provide a sample `date` (e.g., `{ "date": "2025-01-08" }`) to verify that Lambda is sending notifications properly.
2. **Verify Scheduled Invocation**:
    - If you’ve configured EventBridge to trigger the Lambda, ensure that the function is invoked according to the cron schedule.
3. **Check CloudWatch Logs**:
    - Open **CloudWatch Logs** and look at the logs for your Lambda function to validate if everything is working as expected.


---
### Step 8: Verify Notifications

1. **Check for SNS Notifications**:
    - Ensure that emails are sent to the subscribed address when the Lambda function publishes a message to the SNS topic.
2. **Confirm No Errors**:
    - Ensure the Lambda function completes without errors and the notifications are sent correctly.
    - Based on the cron expression cron(0 9-23/2 * * ? *), the Lambda function will be triggered every 2 hours from 9:00 AM to 11:00 PM (in UTC).

At 11AM, I received my email:
[Email Notification]()
  
