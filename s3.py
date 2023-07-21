from s3_core import upload_file
import boto3

if upload_file('querypie.jpeg', 'franfe-raw-cafe-images'):
    print('File successfully uploaded')

else:
    print('File not uploaded')
