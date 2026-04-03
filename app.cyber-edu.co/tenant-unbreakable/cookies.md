# cookies

This is a simple format string vulnerability. We just need to leak the canary in the first walktrough of the loop and then we can inject the payload to jump in the win function.

The canary is at position: `7+108//8+4//8+1` == `21` (the 7 are for the registers, then we calculate the offset of the buffer and the other random variable in the function)

![exploit](cookies-exploit.py)

flag: `CTF{1f94c05a1e6137bac004dc8aaf2d28ff35d7d6568d18495639cded566d9d4d26}`