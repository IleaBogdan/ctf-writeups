# format string 2

To get the flag we need to write in the (global) vartiable **sus** the number 1734437990.
Since the ctf has a format string vulnerability we simply find the address of **sus** and the we can apply the `fmtstr_payload` function from pwntools on it to write the correct value.
We fint that the **sus** is in `.data` (we can write in it) at the address 0x404060. So I made an exploit to find the offset and get the flag. 

![exploit](format_string_2-exploit.py)

flag: `picoCTF{f0rm47_57r?_f0rm47_m3m_99fd82cd}`