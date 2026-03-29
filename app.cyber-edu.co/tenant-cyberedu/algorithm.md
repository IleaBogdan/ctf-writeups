# algorithm

After wenotice that the polinom function only takes in numbers from 0 to 99 we can precalculate all the results.
After that I made a script that checks and tries to reconstruct the input.
(I hate leading 0 errors)

![reconstructor](algorithm-decoder.py)


This script got me at the end: `[ola_th1s_1s_p0l]`
I pasted it into sha256 online tool (with the `[ ]` and got the sha for the flag).

flag: `CTF{267a4401ea64e7167168969743dcc708399e3823d40e4ae37c78d675e281cb14}`