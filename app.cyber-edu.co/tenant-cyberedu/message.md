# message

So after inspecting the decompiled code in  ida we can see that we have use after free.
So we start of with a simple exploit to create a instance in v5 and the delete it.

After we delete it we can use the 'Create message for the admins' function write in s a function address, which btw is also where v5 has it's inspectUser function stored.

When the function from v5 is called, the pointer to it gets dereferenced so we need to find somewhere in the memory where we can find a pointer to the 'win' function.

```
pwndbg> find 0x400000, 0x405000, 0x4013a0
0x402de8
warning: Unable to access 8728 bytes of target memory at 0x402de9, halting search.
1 pattern found.
```


So we have the pointer now. After we write the pointer into s (v5 technically) we can simply call the function.

exploit: [[message_pwn_exploit.py]]

flag: `flag{l1ttle_pwn_F0r_My_fri3nds}`
