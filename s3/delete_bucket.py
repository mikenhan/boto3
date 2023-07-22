'''
S3 Delete Bucket Script
This script is a S3 deletion script.
Please run at your own risk as this action is not reversible

Usage:
    python3 delete_bucket.py

Author:
    Mike Nhan <mike.nhan@gmail.com>
'''


import boto3
from botocore.exceptions import ClientError


def prCyan(skk): 
    print("\033[96m {}\033[00m" .format(skk))

def prRed(skk): 
    print("\033[91m {}\033[00m" .format(skk))

# Function to get user input
# This has a max of 3 tries before
# The script breaks.
def get_user_input(prompt, valid_options):
    tries = 3
    while tries > 0:
        user_input = input(prompt).strip().upper()
        if user_input in valid_options:
            return user_input
        tries -= 1
        prRed(f"You have {tries} remaining.")
    prCyan("Max tries reached.")
    return None

# Function to delete the bucket
def delete_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket(Bucket=bucket_name)
        prCyan(f"{bucket_name} has been deleted.")
    except ClientError as e:
        prRed(e)


# This will be executed only if the script is run directly.
if __name__ == "__main__":
    try:
        question = get_user_input("Do you want to delete a bucket? (Y or N) ", ['Y','N'])
        if question == 'Y':
            bucket_name = input("What is the name of the bucket you wish to delete? ")
            delete_s3_bucket(bucket_name)
        elif question == 'N':
            prCyan("Goodbye.")
    except KeyboardInterrupt:
        prRed("\nOperation interrupted.")
