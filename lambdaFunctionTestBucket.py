import json
import boto3
import botocore

s3 = boto3.resource('s3')
bucket_name = 'eduard-bucket-003'
bucket = s3.Bucket(bucket_name)


def lambda_handler(event, lambda_context):
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)

        print("\n" + " " * 4 + "#" * 18)
        print(" " * 4 + "# Bucket Exists! #")
        print(" " * 4 + "#" * 18 + "\n")

        # return True
        return {
            'statusCode': 200,
            'body': json.dumps('Bucket Exists!')
        }

    except botocore.exceptions.ClientError as e:

        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.

        error_code = int(e.response['Error']['Code'])

        if error_code == 403:
            print("\n" + " " * 4 + "#" * 38)
            print(" " * 4 + "# Private Bucket. Forbidden Access! #")
            print(" " * 4 + "#" * 38 + "\n")

            return {  # return True
                'statusCode': error_code,
                'body': json.dumps('Private Bucket. Forbidden Access!')
            }

        elif error_code == 404:
            print("\n" + " " * 4 + "#" * 26)
            print(" " * 4 + "# Bucket Does Not Exist! #")
            print(" " * 4 + "#" * 26 + "\n")

            return {  # return False
                'statusCode': error_code,
                'body': json.dumps('Bucket Does Not Exist!')
            }

if __name__ == "__main__":
    event, lambda_context = 1, 2
    lambda_handler(event, lambda_context)
