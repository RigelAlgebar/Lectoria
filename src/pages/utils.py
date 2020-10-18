import boto3
from botocore.exceptions import NoCredentialsError

# Document extraction module

def upload_to_aws(file_name, bucket, s3_key):
    s3 = boto3.client('s3', region_name='us-east-2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(file_name, bucket, s3_key)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

