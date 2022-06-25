from Crypto.PublicKey import RSA

fp = open("public.crt", "r")
key = RSA.importKey(fp.read())
fp.close()

print("n: " + hex(key.n))
print("e: " + hex(key.e))
