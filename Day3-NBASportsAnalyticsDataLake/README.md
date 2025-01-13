## NBA Sports Analytics Data Lake Setup

This project demonstrates how to set up a data lake for NBA sports analytics on AWS using the following AWS services:
- **Amazon S3** for storage
- **AWS Glue** for data cataloging and ETL
- **Amazon Athena** for querying data

The project fetches NBA player data from the [SportsData.io API](https://sportsdata.io/), stores it in S3, creates a Glue table, and sets up Athena for querying the data.

## Requirements
- **AWS Account**: You'll need an active AWS account to set up the resources.
- **AWS CLI**: Make sure the AWS CLI is configured with appropriate access to the required services.
- **API Key for SportsData.io**: Sign up for an API key from [SportsData.io](https://sportsdata.io/).
- **Python 3.x**: The script is written in Python and uses the `requests`, `boto3`, and `python-dotenv` libraries.

## Setup Instructions

### 1. Clone the Repository or Download Files

Download the project files including:
- `nba_data_lake_setup.py`: Python script to create the data lake.
- `.env`: Environment file for storing your API key.

### 2. Prepare Environment Variables
Before running the script, create a `.env` file in the root directory of your project to store your API key securely. The `.env` file should contain:

```text
API_KEY=your_sportsdata_io_api_key_here
```

### 3. Install Dependencies

You need the `python-dotenv` library to load the environment variables from the `.env` file.

If you're running the script locally, you can install the required dependencies using `pip`:

```bash
pip install requests boto3 python-dotenv
```

If you're running in AWS CloudShell, `boto3` and `requests` are already available, but you’ll need to install `python-dotenv`:

```bash
pip install python-dotenv
```

### 4. Upload Files to AWS CloudShell (Optional for CloudShell Users)
If you're using **AWS CloudShell**, upload the following files:
- `nba_data_lake_setup.py` (the Python script)
- `.env` (the environment file containing your API key)

### 5. Run the Script in CloudShell or Locally

#### In AWS CloudShell:
1. Open **AWS CloudShell** from the AWS Management Console.
2. Upload your files via the CloudShell terminal.
3. Install `python-dotenv` (if you haven’t already) by running:
   ```bash
   pip install python-dotenv
   ```
4. Run the script:
   ```bash
   python3 nba_data_lake_setup.py
   ```

#### Locally:
1. Ensure your AWS CLI is configured with proper credentials.
2. Run the script:
   ```bash
   python3 nba_data_lake_setup.py
   ```

### 6. Workflow
The script will perform the following actions:
1. **Create an S3 Bucket**: Stores the raw data.
2. **Create a Glue Database**: Catalogs the NBA player data.
3. **Fetch NBA Data**: Fetch player data from the SportsData.io API.
4. **Upload Data to S3**: Uploads the fetched data to the S3 bucket in `raw-data` folder.
5. **Create Glue Table**: Creates an external Glue table for querying the data.
6. **Configure Athena**: Sets up Athena for querying the data in S3.

### 7. Verify Setup
Once the script finishes running, you can verify the following:
- **S3 Bucket**: The NBA data should be available in the `raw-data` folder within the specified S3 bucket.
- **AWS Glue**: Check the AWS Glue console for the database and table created.
- **Athena**: Verify that you can query the data in Athena using the created Glue database.

### 8. Troubleshooting
If you run into issues, check the following:
- Ensure your AWS credentials have the necessary permissions for S3, Glue, and Athena.
- Ensure the `.env` file contains the correct API key format.
- Verify the region specified in the script matches the region for your resources.

### Conclusion
This project demonstrates how to set up a data lake for NBA sports analytics using AWS services. You can extend this setup by adding more data sources, integrating additional analytics tools, or automating data transformations with AWS Glue ETL.

---
