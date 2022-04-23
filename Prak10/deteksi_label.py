from urllib import response
import boto3
import matplotlib.pyplot as plt
import cv2
import os

os.system('cls')

client = boto3.client(
    'rekognition',
    aws_access_key_id = 'AKIATMBRT6Z6VZD4ONIB',
    aws_secret_access_key = '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',
    region_name = 'ap-southeast-1'
)

photo = 'soccer.jpg'
img = cv2.imread(photo)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
with open (photo, 'rb') as source_img:
    source_bytes = source_img.read()

response = client.detect_labels(
    Image = {'Bytes' : source_bytes},
    MaxLabels = 1,
    MinConfidence = 99
)
print(response)

plt.subplot(1,2,1), plt.imshow(img)
plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2), plt.imshow(img)
plt.title('Output'), plt.xticks([]), plt.yticks([])
plt.show()