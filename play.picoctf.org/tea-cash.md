# tea-cash

This ctf does not need a lot of heap exploatation knowledge. If you understant the conncept of having a tcache bin (yeah here is where the name of the ctf comes from) it is simple.

Since the program is allocating 5 heap chuncks of size **0x80** and then frees them, we will have in tcach 5 chuncks of size **0x90** (there is an extra **0x10** for the pointers in the beginig or something like that). So we can simply calculate the offset of each chunk that the program is checking by adding **0x90** to for each of them to the leak we get.
After we send each input we get the flag.

![exploit](tea-cash-exploit.py)

flag: `picoCTF{c4802d4209ab455a3a0336ef58219a78}`