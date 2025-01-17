# Add Numbers Lambda Function

This AWS Lambda function takes two numbers as input and returns their sum.

## Usage

You can invoke this function with the following JSON input:

json
{
    "num1": 5,
    "num2": 10
}



# Upload to S3 Lambda Function

This AWS Lambda function uploads a document or PDF file to a specified S3 bucket.

## Usage

You can invoke this function with the following JSON input:

json
{
    "bucket_name": "your-bucket-name",
    "file_name": "your-file-name.pdf",
    "file_content": "JVBERi0xLjQKJcfs... (base64 encoded content)"
}
