# Cookie Flip

So we have a cookie.
We need to signe the cookie to have from:
```
from:  role=guest;uid=1001
to:    role=admin;uid=1001
```

Since the server encrypts the token using xor we can also apply xor to get change the cookie into what we need. The xor difference between the 2 texts is: `6,17,8,26,26` (guest^admin)

![exploit](Cookie_Flip-exploit.py)

flag: `ALGOLYMP{str3am_c1ph3rs_n33d_1nt3gr1ty}`