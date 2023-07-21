from s3_core import upload_file

upload_result = upload_file('querypie.jpeg', 'franfe-raw-cafe-images')
print('File successfully uploaded' + upload_result)
