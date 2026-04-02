from pwn import *

p=remote("lonely-island.picoctf.net",52066)

p.sendline(b"64-bit")
p.sendline(b"dynamic")
p.sendline(b"not stripped")
p.sendline(b"0x15")
p.sendline(b"0x90")
p.sendline(b"yes")
p.sendline(b"fgets")
p.sendline(b"win")
p.sendline(b"buffer overflow")
p.sendline(b"0x7b")
p.sendline(b"NX")
p.sendline(b"ROP")
p.sendline(b"0x401176")

p.interactive()