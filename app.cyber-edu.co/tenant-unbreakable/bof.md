# bof

This is a simple buffer overflow vulnerability. 
We send 312 random bytes to overflow the buffer and rbp and then we simply send `p64(ret)+p64(flag_addr)`

![exploit](bof-exploit.py)

flag: `ctf{c7fabc6bfe7e4b40b78244854f95f089414bb8354e021f89fe632202bb35ef99}`