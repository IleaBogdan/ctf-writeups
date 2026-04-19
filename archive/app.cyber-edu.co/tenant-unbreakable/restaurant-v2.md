# restaurant-v2

Ok this ctf tests our skills and understanding of 2 other pwn ctfs. ([under-attack](under-attack.md) and [restaurant](restaurant.md))

I made a writeup for both I recomand you to check them out.
But if you are lazy like me and just want to read from this writeup well I shall give you an explination.

So we can split the ctf in 2 parts:
 - 1. leaking the variable flag, that has a random value from urandom, so we can get to the second part
 - 2. exploit leaking libc and a buffer overflow vulnerability with `one_gadget`

#### Part 1)
So I splited the 2 problems in 2 functions.
The first one needs us to leak the urandom number. We can do that via the format-string attack. To do so we need to figure out the index to put in the pointer we want to leak. (eg: %100$p)

After running the same main function (modified a little) I found out that the pointer offset I am looking is at index 9.
[copy-test](restaurant-v2-copy-test.cpp)


#### Part 2)
Now that we have moved on to the second part if the ctf, we can leak the libc address of `puts` via the `GOT` table. We also need to make sure to call back the function we are in so that we don't get seg fault.

After we leak the address for `puts` in libc we can simply open the libc in gdb and run `p puts` and we will get the offset of puts.
After that we can get libc base.

With libc base I looked at the `one_gadget`'s in libc and found 2 interesting ones:
```c++
0x4f302 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL || {[rsp+0x40], [rsp+0x48], [rsp+0x50], [rsp+0x58], ...} is a valid argv

0x10a2fc execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL || {[rsp+0x70], [rsp+0x78], [rsp+0x80], [rsp+0x88], ...} is a valid argv
```

Since our buffer is starting at `rsp+0x0` I tried setting the first **0x40** (64) bytes to **\x00**, it did not work for some reason. However with **0x70** (112) bytes as **\x00** worked just fine.

![exploit](restaurant-v2-exploit.py)

flag: `CTF{04134a331cd5bed41dc418c04854ac3fd7e03148f0e61d74d61508f19b7c5933}`