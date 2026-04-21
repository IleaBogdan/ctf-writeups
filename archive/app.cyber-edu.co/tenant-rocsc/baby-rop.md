# baby-rop

This ctf is a prime example of simple buffer overflow. 
The logic in the **sub_401176** function can be ignored at most. 
We only need to keep in mind that there is a **gets** function that reads into *v1* and there are *32* **__int64** variables on the stack.
So we will leak the libc with the classic got leak and then we will call **system** of `/bin/sh` and get shell.

![exploit](baby-rop-exploit.py)

flag: `ECSC{c6e202f0d761b296c2fe9dbebc5169a892833cffa65399fee585b532eca3fcac}`