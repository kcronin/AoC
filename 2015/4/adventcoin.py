#!/usr/bin/env python3

import hashlib

key = "yzbqklnj"

i = 1

while True:
    md5hash_prefix = hashlib.md5((key + str(i)).encode()).hexdigest()[:6]
    if md5hash_prefix == "000000":
        print(i)
        break
    i += 1
