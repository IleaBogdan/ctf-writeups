# heap 1

For this ctf to get the flag we simply have to use the fact that we have a heap overflow. We can read any amount of bytes in the first variable that is a pointer on the heap and with that we can eventually overwrite over the second one that is right under the first one.
To get the flag we need to set the second one to be `pico`. So we send 32 random bytes and then the word pico and we can get the flag.

![exploit](heap_1-exploit.py)

flag: `picoCTF{starting_to_get_the_hang_e9fbcea5}`