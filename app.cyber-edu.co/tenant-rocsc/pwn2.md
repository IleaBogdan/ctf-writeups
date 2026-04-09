# pwn2

This is a simple fmt exploit ctf, but I was dumb and it took me to long to solve it.
The main idea is we need to write somewhere in the binary the string `/bin/sh` and then we need to write in the variable `cmd` the pointer where we stored `/bin/sh`.

With pwntools in python we can use the function: fmtstr_payload to write int values in different memory addresses.
For example:
```python
payload=fmtstr_payload(offset,{some_mem_addr:100})
```

Now in the `some_mem_addr` we will have the value 100.

Using that we can make a payload like this:
```python
payload=fmtstr_payload(6,{0x404048:0x404060,0x404060:0x68732f6e69622f2f})
```
(After testing differend offsets with %i$p I found that my input is at the offset 6 on the stack)
This payload writes the string `//bin/sh` in hex with little endian applied to it at some writable memory address (0x404060) and then writes that memory address in 0x404048 that is the memory addres to the cmd string pointer, so that when **system(cmd)** is called we will have it call `/bin/sh`.

![exploit](pwn2-exploit.py)

flag: `CTF{c74cd752838ec12c1004b825e39993452f3e2480f1869a8dac788fe352bdce04}`