### Create the frontend folder and add the following files:
- index.html: The main webpage for your CV.
- style.css: Styling for your CV.
- script.js: Handles form submission logic.

### Create the backend folder and add the following files:
- server.js: Contains the backend code.

### Initialize the backend project:

Navigate to the backend directory:
cd backend
npm init -y

Install dependencies:
npm install express body-parser mysql2

- Add code to the apps list above 

### Prepare for deploying your full-stack CV application using AWS services with Terraform and GitHub Actions.

#### Terraform set-up for AWS resources 
You will use Terraform to set up the infrastructure on AWS. Since you're deploying a static website, you will mainly need an S3 bucket for hosting the HTML, CSS, and JavaScript files. You may also want to use CloudFront for content delivery and a Route 53 domain for a custom URL.

- First, you'll need to install [Terraform](https://developer.hashicorp.com/terraform/install) if you haven't already. 
- Verify your installation
```bash
terraform -v
```
- Initialize your Terraform configuration in your project. 
You should keep your Terraform files in a dedicated directory (e.g., terraform/).

```bash
your-repo/
├── terraform/
│   ├── main.tf         # Your main infrastructure configuration
│   ├── variables.tf    # Declare any variables that will reference throughout your terraform code (e.g., bucket names, regions)
│   ├── outputs.tf      # Outputs from your configuration (e.g., S3 bucket URL)
│   └── provider.tf     # AWS provider configuration (AWS region and profile)
└── README.md
```



Terraform Doesn't Automatically Create the Bucket for State Management so you have to create the state bucket in AWS
- Create a bucket in S3
- Allow public access within bucket
- Add a bucket policy to allow IAM role or user to access it 

Once you've added the configuration, initialize Terraform and apply it:
terraform init      # Initializes the working directory
terraform validate (Success! The configuration is valid.) # validate the configuration
terraform plan      # create an execution plan 
terraform apply     # Deploys the S3 bucket and other 


#### GitHub Actions Setup for CI/CD
Now, you'll set up GitHub Actions to automate the deployment to AWS. The workflow will upload your website files to the S3 bucket whenever you push to the repository.

Steps:

Create a .github/workflows directory in your repository if it doesn't exist.
Create a deploy.yml file to define the deployment process.
mkdir -p .github/workflows
touch .github/workflows/deploy.yml



#### Add AWS Credentials to GitHub Secrets
To securely deploy your application using GitHub Actions, you need to store your AWS credentials (Access Key ID and Secret Access Key) as GitHub Secrets:

Go to your GitHub repository settings.
Under Secrets > New repository secret, add the following secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY


#### Deploy and Test
Commit and push your changes to the main branch. The GitHub Actions workflow will trigger automatically, deploying your website to the S3 bucket.
After the deployment, you can visit the provided S3 URL or your custom domain (if using Route 53) to view your live CV application.