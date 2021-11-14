# https: // kshitizkr.medium.com/babyencryption-htb-write-up-8d7d191369b3

def decryption(message):
    pt = []
    for char in message:
        char = char - 18
        char = 179 * char % 256
        pt.append(char)
    return bytes(pt)

with open('msg.enc') as f:
    message = bytes.fromhex(f.read())

decrypted = decryption(message)
print(decrypted)
