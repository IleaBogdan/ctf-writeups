# zebra-lib

Since the ctf is named zebra-lib, and is a misc ctf I googled zebra-lib, but I was getting some random results that were not helping. Only at around page 3-4 of google I found something interesting: `zlib`

`zlib is a widely used, open-source, lossless data-compression library designed for cross-platform efficiency`

Bingo.
The url was giving us a string in base64 but when we decode it from base64 we were getting garbage, however, if we applyed the zlib decode on the base64 decoded string we got some readable text.

So I made a simple python exploit to automatically reply to the server with de decoded data.
![exploit](zebra-lib-exploit.py)

flag: `CTF{a7550246d72f8c7946a9248b3b9eee93461ac30f53ac8ca9749c9590b4ed1a2b}`