import boto3
from random import randint

x = [randint(0, 9) for p in range(0, 10)]

s3 = boto3.resource('s3')
bucket_name = 'eduard-bucket-00' + chr(x);

def createBucket(bucket_name):
    if s3.lookup(bucket_name) is None:
        bucket = s3.create_bucket(bucket_name)  # Bucket Don't Exist
    else:
        bucket = s3.get_bucket(bucket_name)  # Bucket Exist


if __name__ == "__main__":
    createBucket(bucket_name)
