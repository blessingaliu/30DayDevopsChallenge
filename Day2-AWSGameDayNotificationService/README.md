
---

# 🌤️ AWS Game Day Notifications Service 

Creating an Event-driven Game Day Notification solution utilizing AWS serverless services including AWS Lambda, Amazon SNS and Amazon EventBridge with an external API. I used AWS CloudFormation to automate the rest of the infrastructure after setting up the SNS Notification and Subscription (step by step guidance is documented in my [howto.md](https://github.com/blessingaliu/30DayDevopsChallenge/blob/main/Day2-AWSGameDayNotificationService/howto.md))

### System Architecture Overview

```plaintext
                  +-------------------+
                  | SportsData.io API |
                  +-------------------+
                           |
              Fetch Game Data (API Request)
                           |
                +--------------------+
                | AWS Lambda Function |
                +--------------------+
                           |
               Process Game Data & Format
                           |
          +--------------------------------+
          | Amazon Simple Notification Service |
          +--------------------------------+
              /                    \
     SMS Notification       Email Notification
         (Subscribers)         (Subscribers)

Scheduled Trigger:                 Secure Access:
+----------------------+      +---------------------------+
| Amazon EventBridge   |      | IAM Roles & Policies       |
| Rule (e.g., 30 mins) |      | - Lambda Execution Role   |
+----------------------+      | - EventBridge Permissions |
                              +---------------------------+
```


---

## 🛠️ Prerequisites

Before you run the application, you’ll need the following:

- 🐍 **Python 3.x** installed on your local machine.
- 🛠️ **AWS CLI** installed and configured with your AWS credentials.
- 🌍 **SportsData.io API Key** (for fetching sports data).
- ☁️ **AWS Account** with access to services like **Lambda, CloudFormation**.

---

## **Roadmap for Building the Notification System**

1. **Set Up the SNS Topic**
    - Create an SNS topic (`gameday`) for notifications.
    - Add subscriptions (email/SMS) to the topic.
2. **Set Up the IAM Role for Lambda**
    - Create an IAM Role with:
        - Permissions to publish to the SNS topic.
        - Basic Lambda execution permissions.
3. **Create the Lambda Function**
    - Write a Lambda function in Python to:
        - Query the SportsData.io API.
        - Process the game data and filter events.
        - Publish notifications to the SNS topic.
4. **Store API Keys Securely**
    - Use AWS Secrets Manager to store and retrieve the SportsData.io API key, I will be storing the Keys in Environment variables within the Lambda Function.
5. **Integrate EventBridge Scheduler**
    - Set up an EventBridge rule to invoke the Lambda function on a schedule (e.g., every 30 minutes on game day).
6. **Outputs for Verification**
    - Add outputs to display:
        - SNS Topic ARN.
        - Lambda Function Name.
        - EventBridge Rule ARN.
     
---

## What I've Learned:
- I have successfully integrated AWS Lambda with SportsData.io API to fetch NBA game data.
- The use of Amazon SNS allowed me to send SMS and Email notifications based on game day events, ensuring subscribers are informed.
- I learned that SNS subscriptions for email need to be confirmed before running the Lambda function. Therefore, it was important to set up SNS first and ensure that email subscribers confirm their subscriptions, so notifications could be delivered properly when the Lambda function executed.
- With Amazon EventBridge, I created a scheduled event to trigger the Lambda function periodically, ensuring that the notifications are sent out at the right times.
- AWS CloudFormation enabled me to automate and manage the entire infrastructure stack efficiently.
- I implemented IAM roles and policies to ensure that each service in the architecture has the appropriate permissions to perform the required actions securely, such as Lambda’s access to SNS and EventBridge’s permissions to trigger the function.
