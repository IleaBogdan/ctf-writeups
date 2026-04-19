# mussel

This is a simple buffer-overflow ctf.
The program reads 128 bytes in a 32 bytes buffer.

I had some truble pwniniting the binary with the libc so I did the ctf with the unlinked binary.
After leaking libc with the `puts(got_puts)` trick we can calculate the offset of puts from the libc by running `gdb ./libc.so.6` and the in the gdb termina we run `p puts` and get the offset of puts.

After that I looked in the one_gadgets the libc had and found something interesting:
```
0x41320 execve("/bin/sh", rsp+0x30, environ)
constraints:
  address rsp+0x40 is writable
  rax == NULL || {rax, "-c", rbx, NULL} is a valid argv

0x41374 execve("/bin/sh", rsp+0x30, environ)
constraints:
  [rsp+0x30] == NULL || {[rsp+0x30], [rsp+0x38], [rsp+0x40], [rsp+0x48], ...} is a valid argv

0xd6e77 execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL || {[rsp+0x70], [rsp+0x78], [rsp+0x80], [rsp+0x88], ...} is a valid argv
```

For the second gadget we only need **rsp+0x30** to be null (\x00), our input starts at **rsp+0x0** and we can send 128 bytes of data (***hex(128)==0x80***) so we can set the null byte at **rsp+0x30** with no problem and get shell.

Also note after you get shell:
 - You are in `/`
 - I found the flag to be in `/home/ctf` 

![exploit](mussel-exploit.py)

flag: `UNR{many_faced_god}`