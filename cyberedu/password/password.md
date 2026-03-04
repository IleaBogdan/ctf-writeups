
So when I saw a .pyc file I send it to the uncompyle6 tool.
> uncompyle6 chall.pyc > chall.py

After inspecting the python code we can see the password was `Pass999990000!!!))))`.
Then if we run the scrip and input the password we get the flag.

flag: `DCTF{09fa7ab70e9aa4d3142a6ad4b55ea5b1a436b5361929d62e0805934d8659eadd}`