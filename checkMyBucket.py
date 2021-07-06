import boto3
import botocore

s3 = boto3.resource('s3')
bucket_name = 'eduard-bucket-002'
bucket = s3.Bucket(bucket_name)

def check_bucket(bucket):
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
        print("Bucket Exists!")

        return True

    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code'])
        if error_code == 403:
            print("Private Bucket. Forbidden Access!")

            return True
        elif error_code == 404:
            print("Bucket Does Not Exist!")

            return False

if __name__ == "__main__":
    check_bucket(bucket)
