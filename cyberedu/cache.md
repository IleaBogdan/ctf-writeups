# cache

The ctf looks simple at first.
All we need to do is:
```python
makeUser(b'A'*8)
deleteUser()
makeAdmin()
editUserName(b'A'*8+p64(0x40084a))
printAdminInfo()
```
But after doing that, I tested it on remote and was greeted with a rickroll and a **try harder** message. 

So the other variant we have is:
 - leaking libc (somehow)
 - double free
 - overwriting ***malloc_hook*** with a one_gadget
One idea I've got from the ctf name is tcache poisoning, since the ctf is named cache.
And after inspecting the main_arena (doing vis in gdb while running the program) I saw that it places the freed chunks in tcache bins.
So I looked at different memory addresses to find out where I can redirect the malloc alocation to then print it with the `Print Student Name` function.

After inspecting the source code for malloc in this libc (https://elixir.bootlin.com/glibc/glibc-2.27/source/malloc/malloc.c) I saw that I can simply combine the use after free vulnerability and get the ability to simply do a malloc, a free and then edit it with the address I want to malloc into. After that I malloc once to remove the first malloc and then malloc again to malloc in the poisoned address. The poisoned address has the format of: ***`0x00000000 0xSome_libc_address`*** 
So if we send a payload with strlen <=8 we can keep the second part that is the libc address. 
After that we simply print the name and this will leak our libc address. The address I found was in the got table, I belive right after the end (maybe, I am not sure): 0x602078

After we leak the libc address we calculate the offset to be `4114272` and the we get libc base.
Keep in mind that this leak is working only 50% of the time, just rerun the script.

After getting the libc base we try out the 4 one_gadgets just in the same way we tried to do the get_flag function. (You could put it into malloc hook but it takes to long to do so.)

exploit:
[[cache-exploit.py]]

flag: `CTF{ab7bdaa3e5ed17ed326fef624a2d95d6ea62caa3dba6d1e5493936c362eed40e}`