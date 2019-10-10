from google.cloud import storage
import os
import google
gae_dir = google.__path__.append('/home/ganesh/my-projects/imp_files/')

from google.appengine.ext import blobstore 
from google.appengine.api import images
import webapp2

# import google.appengine 

storage_client = storage.Client.from_service_account_json("/home/ganesh/Downloads/keelaa-1535435701928-17377c1fbdda.json")

# print(list(storage_client.list_buckets()))

bucket = storage_client.get_bucket("keelaa-images")
blob = bucket.blob("ganesh")
blob.upload_from_filename("/home/ganesh/1.jpg")

#returns a public url
print(blob.public_url,type(blob.public_url))
# serving_url = images.get_serving_url(filename=blob.public_url)
# print(serving_url)
img = images.Image(blob_key=blob)
img.resize(width=80, height=100)
img.im_feeling_lucky()
thumbnail = img.execute_transforms(output_encoding=images.JPEG)
url = images.get_serving_url(
    blob, size=150, crop=True, secure_url=True)
print(url,"/////////")
