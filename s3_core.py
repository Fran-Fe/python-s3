import logging
import boto3
from botocore.exceptions import ClientError
import os

aws_access_key_id = '',
aws_secret_access_key = 'YOUR_SECRET_KEY',
region_name = 'us-west-1'


def upload_file(file_name, bucket, object_name=None) -> str:
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3',
                             aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key,
                             region_name=region_name)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)

    except ClientError as e:
        logging.error(e)
        return e

    return response


def upload_file(file_name, bucket, object_name) -> bool:
    s3_client = boto3.client('s3',
                             aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key,
                             region_name=region_name)

    s3_client.download_file(bucket, object_name, file_name)
