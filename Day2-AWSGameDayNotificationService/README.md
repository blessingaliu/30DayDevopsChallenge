
---

# 🌤️ AWS Game Day Notifications Service 

Creating an Event-driven Game Day Notification solution utilizing AWS serverless services including AWS Lambda, Amazon SNS and Amazon EventBridge with an external API. I used AWS CloudFormation to automate the rest of the infrastructure after setting up the SNS Notification and Subscription. Have a look at my [blogpost](https://blessingaliu.hashnode.dev/day-2-building-a-real-time-nba-game-day-notification-system-with-aws-lambda-sns-and-eventbridge) for detailed step by step guidance.

### System Architecture Overview
![Design Diagram](https://github.com/blessingaliu/30DayDevopsChallenge/blob/203d4f8159f478d01c97c11bc95b3d3328a58312/NBA%20Game%20Day%20Alerts%20Application.drawio.png)


---

## 🛠️ Prerequisites

Before you run the application, you’ll need the following:

- 🐍 **Python 3.x** installed on your local machine.
- 🛠️ **AWS CLI** installed and configured with your AWS credentials.
- 🌍 **SportsData.io API Key** (for fetching sports data).
- ☁️ **AWS Account** with access to services like **Lambda, CloudFormation**.

---

## What I've Learned:
- I have successfully integrated AWS Lambda with SportsData.io API to fetch NBA game data.
- The use of Amazon SNS allowed me to send SMS and Email notifications based on game day events, ensuring subscribers are informed.
- I learned that SNS subscriptions for email need to be confirmed before running the Lambda function. Therefore, it was important to set up SNS first and ensure that email subscribers confirm their subscriptions, so notifications could be delivered properly when the Lambda function executed.
- With Amazon EventBridge, I created a scheduled event to trigger the Lambda function periodically, ensuring that the notifications are sent out at the right times.
- AWS CloudFormation enabled me to automate and manage the entire infrastructure stack efficiently.
- I implemented IAM roles and policies to ensure that each service in the architecture has the appropriate permissions to perform the required actions securely, such as Lambda’s access to SNS and EventBridge’s permissions to trigger the function.
