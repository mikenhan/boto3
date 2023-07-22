'''
S3 Create Bucket Script
This script is a S3 bucket creation script.

Usage:
    python3 create_bucket.py

Author:
    Mike Nhan <mike.nhan@gmail.com>
'''

import boto3
from botocore.exceptions import ClientError

def prCyan(skk): 
    print("\033[96m {}\033[00m" .format(skk))

def create_s3_bucket(bucket_name, region):
    s3 = boto3.resource('s3')
    try:
        s3.create_bucket(
            ACL='private',
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            },
            ObjectOwnership='BucketOwnerPreferred'
        )
        prCyan(f"{bucket_name} has been created in {region}")
    except ClientError as e:
        print(e)

if __name__ == "__main__":
    try:
        bucket_name = input("Please provide me the name of the bucket you wish to create: ")
        region = input("Please provide the AWS region you wish to create the bucket in: ")
        create_s3_bucket(bucket_name, region)
    except KeyboardInterrupt:
        print("\nOperation interrupted.")
