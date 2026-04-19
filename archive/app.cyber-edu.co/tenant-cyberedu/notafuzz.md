# notafuzz

solution:
 - the vulnerability was that it loops from 1 to 9999 and when it reaches the index 3, your input is put in a printf (example: printf(format);)
 - so you can leak values from the stack
 - we will leak memory addreses (%p)

exploit:
 - I made a python exploit that opens a connection to the server and sends a payload to read what is at index i on the stack
 - the range the flag is in is from 135 to 153
 - at the end we need to remove all the X chars since they are not part of the flag, and just there to make the string we read longer. 

exploit:
[[nodafux-exploit.py]]

flag: `ctf{fad65340180f6b4c6f49dad138daeed447cf23f994635481f92551f05dbc6070}`