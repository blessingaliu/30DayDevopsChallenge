
---

# 🌤️ AWS Game Day Notifications Service 

Creating an event-driven Game Day Notification solution utilizing AWS serverless services including AWS Lambda, Amazon SNS and Amazon EventBridge with external APIs

You can add the diagram into your Markdown file using code blocks for better formatting. To do that, you can use the following approach:


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

