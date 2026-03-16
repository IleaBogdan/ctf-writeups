# function-check

In this ctf we have a format string vulnerability, but we don't need to get pie or canary or anything like that, we just have to change the value of a global variable. Since the ctf has no pie it is easy. (If we would have had pie we would have had to recall the function and do some more complex stuff, but not in this case.)

Anyways the idea is to overwrite the variable __demo_3187__ at the address: __0x0804a030__.
All we need to do is remember the %n property of the format string vulnerability. 

We first find out at what offset on the stack is our input by doing a lot of %p until we can see the hex value of out %p. I calculated it to be at *3+(200+212)//8*=**54** (don't ask, I don't know what was in my mind when I figured out that was the offset).

Now we can simply do: ```payload=b'\x30\xa0\x04\x08%14x%54$n'```
This payload means we write in the value of \x30\xa0\x04\x08 (0x0804a030, our address) 14 bytes of padding. The %54$n redirects the printf function to put in the pointer at the 54 offset on the stack the amount of bytes we have, or so I read somewhere. I tried doing %32x but it failed and after testing multiple values only 14 worked. 

script:
[[function-check-exploit.py]]

flag: `CTF{1f94c04a1e6037ba4004dc8eaf2d28ff35d7d6568d17495639cded566a9d4d26}`