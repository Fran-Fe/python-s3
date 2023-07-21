from s3_core import download_file

try:
    download_file('querypie.jpeg', 'franfe-raw-cafe-images', 'querypie.jpeg')
except Exception as e:
    print('File successfully uploaded')
