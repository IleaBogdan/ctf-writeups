# notafuzz

After analysing the binary with ida, I saw that at the third input it puts it into a printf and not puts. This is a major vulnerability since it is the ***Format String Vulnerability***. So after calculating some offsets on where the v7 input could be, I made a script to leak the pointer addresses of the flag. 
I got this offsets that leak the pointers: `i+9+1008//8` (i is a number between 0 and 20)

After leaking everything we need to remove the XXXX chars from the leaks since they are there just to get in our way.

exploit:
![notafuzz-exploit.py](notafuzz-exploit.py)

flag: `ctf{fad65340180f6b4c6f49dad138daeed447cf23f994635481f92551f05dbc6070}`
