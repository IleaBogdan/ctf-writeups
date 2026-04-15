# cacamaca

The binary reads shellcode ant then executes it. There is a function that checks for some instructions in our payload:
```c
__int64 __fastcall forbidden(__int64 a1)
{
  unsigned __int64 i; // [rsp+10h] [rbp-10h]
  for ( i = 0; i <= 126; ++i )
  {
    if ( *(_BYTE *)(a1 + i) == 0xF && *(_BYTE *)(i + 1 + a1) == 5
      || *(_BYTE *)(a1 + i) == 0xF && *(_BYTE *)(i + 1 + a1) == 0x34
      || *(_BYTE *)(a1 + i) == 0xCD && *(_BYTE *)(i + 1 + a1) == 0x80 )
    {
      puts("Forbidden spell detected!");
      return 1;
    }
  }
  return 0;
}
```

The instructions it filters out are:
```sh
$ echo -ne "\xF\x5" | ndisasm -b64 -
00000000  0F05              syscall
$ echo -ne "\xF\x34" | ndisasm -b64 -
00000000  0F34              sysenter
$ echo -ne "\xCD\x80" | ndisasm -b64 -
00000000  CD80              int 0x80

```

So we need to find a way to do a syscall without using the syscall on 64 or 32 bits.
I looked up some methods to bypass that (maybe a syscall on 16 bits), but no luck.
However I have found this: https://stackoverflow.com/questions/70190899/how-to-use-a-syscall-in-a-shellcode-without-use-syscall-or-sysenter-for-linu

So since we have a mmaped memory region with 7 (read, write, execute) we can use our code to modify the code inside it before it gets executed. So we can store the **syscall** bytes xored with **0xAAAA** and our code to go at the region in memory and xor them back to restore the syscall. This way we bypass the checker.

![exploit](random_luma_ctf_1-exploit.py)

flag: `CTF{Luma_iti_da_respect_kendama}` (There is no flag for this ctf since I just got the binary on discord from a friend so I made up a flag)