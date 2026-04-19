import base64
from pwn import *

junk_data=[
b'0x4b4e554a00007fff',
b'0x517c7c7c4b4e554a',
b'0x4f6d687a65475231',
b'0x59684e7a59784d54',
b'0x4e6a68544d6a6454',
b'0x596946575a7a4557',
b'0x596852474f30676a',
b'0x4d3263445a776b54',
b'0x4e7a51575a336b54',
b'0x596868444e784144',
b'0x4f6c526d4d776354',
b'0x4f3449444f6b5654',
b'0x5a6842544f784947',
b'0x554a7c7c7c395657',
b'0x554a4b4e554a4b4e',
b'0x0000000000004b4e',
]

unjunked = [unhex(junk[2:]) for junk in junk_data]
print(unjunked)

idk_what_junk=[]
for unjunk in unjunked:
    idk_what_junk.append(unjunk[::-1])
cflag=b''.join(idk_what_junk)
print(cflag)

print(base64.b64decode(cflag)[6:-9])