import requests
import cv2
import json

response = requests.post('http://127.0.0.1:5000/uploader', files = {'file': open("./demo/test.jpg",'rb')})

print(json.loads(response.text))