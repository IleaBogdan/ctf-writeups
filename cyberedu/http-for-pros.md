# http-for-pros

This is a SSTI injection ctf.
The main idea is that some keywords are blocked. 
A way to bypass them is to insert our payloads inside of headers or cookies or get params.
I chose the cookie aproache since I could make a python exploit.

The main idea is that in the get param named content we can redierect it to some costum cookies we make.

exploit:
![[http-for-pros-exploit.py]]

flag: `CTF{75df3454a132fcdd37d94882e343c6a23e961ed70f8dd88195345aa874c63e63}`