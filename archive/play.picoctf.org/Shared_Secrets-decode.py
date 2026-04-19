from Crypto.Util.number import getPrime
from random import randint

g,p,A,b,enc=0,0,0,0,0
with open("message.txt","r")as file:
    lines=file.readlines()
    g=lines[0].split(" = ")[-1]
    p=int(lines[1].split(" = ")[-1])
    A=int(lines[2].split(" = ")[-1])
    b=int(lines[3].split(" = ")[-1])
    enc=lines[4].split(" = ")[-1]

ct=bytes.fromhex(enc)
# print(ct)

# p = getPrime(1048)
shared = pow(A, b, p)

# print(shared)
print(bytes([x ^ (shared % 256) for x in ct]))