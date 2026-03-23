# shellcode

We can see that the ctf leaks us the pointer of buf and the name of the ctf just gives me the idea that maybe we can inject stuff in the buffer and then move the execution to that one. After running checksec on the file I see that the `NX` is not enabled. So yeah thats the idea.

I made a simple exploit to inject assembly code into the buffer and then move the execution to it since there is no canary and we can overflow the buffer.

![exploit](shellcode-exploit.py)
flag: `CTF{a32b7e7a25ff503c5440757f5e65f94b5178adc3e36d886c885a39044eccc887}`