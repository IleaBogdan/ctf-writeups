# restaurant

After we take a look in ida to the decompiled program we see that if want the option 3 in the menu we get to a function that is vulnerable to buffer overflow since it reads in our small buffer with `gets`.
After that we can leak the GOT table address of `puts` and `printf` to easily find the libc (with https://libc.rip/) to get shell.

I found the write libc to be: `libc6_2.27-3ubuntu1.4_amd64`

So after compuiting the libc_base I made the payload that grants me shell.

![exploit](restaurant-exploit.py)

flag: `CTF{33be4238b68642a4c3f97d10cfa034764e0b6d9707d6970f581200e2b7bcbfc0}`