# coding: utf-8
import boto3
session = boto3.Session('cgawspython')
session = boto3.Session(profile_name='cgawspython')
s3 = session.resource('s')
s3 = session.resource('s')
get_ipython().run_line_magic('clear', '')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='fahdvideolyzer')
from pathlib import Path
pathname = '/Users/fahd/Downloads/Blurry Video Of People Working.mp4'
pathname = '~/Downloads/Blurry Video Of People Working.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path),str(path.name))
rekognition_client = session.resource('rekognition')
rekognition_client = session.client('rekognition')
rekognition_client = session.resource('rekognition')
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket':bucket.name, 'Name': path.name}})
bucket = s3.create_bucket(Bucket='fahdvideolyzer')
bucket.upload_file(str(path), str(path.name))
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket':bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
job_id
result = rekognition_client.get_label_detection(Job_Id=job_id)
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['Labels']
result.keys()
result['Labels'].keys()
result.keys['Labels']
get_ipython().run_line_magic('save', 'label-detection.py 1-30')
