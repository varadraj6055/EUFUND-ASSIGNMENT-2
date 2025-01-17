
### 2. AWS Lambda Function to Store a Document or PDF File in an S3 Bucket

#### `upload_to_s3/lambda_function.py`


import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket name and file details from the event
    bucket_name = event['bucket_name']
    file_name = event['file_name']
    file_content = event['file_content']  # Base64 encoded content
    
    # Decode the file content
    decoded_file_content = base64.b64decode(file_content)
    
    # Upload the file to S3
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=decoded_file_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'File {file_name} uploaded to {bucket_name} successfully!'
        })
    }