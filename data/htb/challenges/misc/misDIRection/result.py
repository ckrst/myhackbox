import os
import base64
chars = [''] * 100
dir = os.path.dirname(os.path.realpath(__file__))
dirs = os.listdir(dir + "/.secret")
for d in dirs:
    cd = os.listdir(dir + "/.secret/" + d)
    for c in cd:
        num = int(c)
        chars[num] = d
textFromSecret = ''
for i in chars:
    if i != '':
        textFromSecret += i
flag = base64.b64decode(textFromSecret)
print(flag)