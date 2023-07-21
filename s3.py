from s3_core import upload_file
import boto3

upload_result = upload_file('querypie.jpeg', 'franfe-raw-cafe-images')
print('File successfully uploaded' + upload_result)
