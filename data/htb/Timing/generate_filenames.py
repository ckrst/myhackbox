import time
import hashlib

while True:
    print(f"{hashlib.md5('$file_hash'.encode()+str(int(time.time())).encode()).hexdigest()}")
    time.sleep(1)