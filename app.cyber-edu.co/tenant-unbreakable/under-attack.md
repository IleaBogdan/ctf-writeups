# under-attack

This ctf tests our skills to exploit `Format string attack`. (hint in the name of the binary)
So I first made a copy of the ctf with an infinit while loop to allow me to retry the same random number and see the exact offset in the ctf.
![under-attack-copy](under-attack-copy.cpp)


For some stupid reason the index in my copy was offseted with one (probably since I compiled it with g++ and not gcc or some stuff like that).

Anyways after seeing that at index 11 I get the stack canary I subtracted 2 from 11 and got 9, and at index 9 we will have out variable flag in hex that we can decode and then resend it to get the shell.

![exploit](under-attack-exploit.py)

flag: `CTF{09aea10d4ab225782586c58698e41c6599c721ec4928ce6a38203ba32ca80507}`