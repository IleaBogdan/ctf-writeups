from pwn import *
import hashlib
from tqdm import tqdm

# List of supported hash types
hash_names = [
    'blake2b', 
    'blake2s', 
    'md5', 
    'sha1', 
    'sha224', 
    'sha256', 
    'sha384', 
    'sha3_224', 
    'sha3_256', 
    'sha3_384', 
    'sha3_512', 
    'sha512',
]

def crack_hash(hash, wordlist, hash_type=None):
    hash_fn = getattr(hashlib, hash_type, None)
    if hash_fn is None or hash_type not in hash_names:
        raise ValueError(f'[!] Invalid hash type: {hash_type}, supported are {hash_names}')
    total_lines = sum(1 for line in open(wordlist, 'r',encoding="latin-1"))
    # print(f"[*] Cracking hash {hash} using {hash_type} with a list of {total_lines} words.")
    with open(wordlist, 'r', encoding="latin-1") as f:
        for line in tqdm(f, desc='Cracking hash', total=total_lines):
            if hash_fn(line.strip().encode()).hexdigest() == hash:
                return line
            

p=remote("verbal-sleep.picoctf.net",56641)

wordlist="/home/ileab/Wordlists/rockyou.txt"

p.recvuntil(b"hash: ")
hash=p.recvuntil(b"\n")[:-1].decode()
print(hash)
passwd=crack_hash(hash,wordlist,"md5")
print("Passwd: "+passwd)
o=p.recv()
p.send(passwd.encode())

p.recvuntil(b"hash: ")
hash=p.recvuntil(b"\n")[:-1].decode()
print(hash)
passwd=crack_hash(hash,wordlist,"sha1")
print("Passwd: "+passwd)
o=p.recv()
p.send(passwd.encode())

p.recvuntil(b"hash: ")
hash=p.recvuntil(b"\n")[:-1].decode()
print(hash)
passwd=crack_hash(hash,wordlist,"sha256")
print("Passwd: "+passwd)
o=p.recv()
p.send(passwd.encode())

# print(o)
p.interactive()