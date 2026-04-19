from pwn import *

not_blacklisted=[]
blacklisted=[]

def check(ch):
    p=remote("34.141.22.126",30860)
    # sleep(0.01)
    p.sendline(ch)
    sleep(0.1)
    res=p.recv()
    print(ch, " --- ", res)
    sleep(0.1)
    if b"Blacklisted" in res:
        blacklisted.append(ch)
    else:
        not_blacklisted.append(ch)
    p.close()
for ch in range(33,127):
    check(chr(ch).encode())
check(b"/bin/sh")
check(b"import")
check(b"self")
check(b"_")
check(b"__")
print(blacklisted)
print(not_blacklisted)

with open("blacklist.txt","w")as file:
    file.write("blacklisted:\n")
    for c in blacklisted:
        file.write(c.decode()+",")
    file.write("\n\n\nallowed:\n")
    for c in not_blacklisted:
        file.write(c.decode()+",")
    