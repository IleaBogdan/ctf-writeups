# Input Injection 2

This ctf is based on a heap overflow vulnerability.
The idea is that it allocates on the heap **0x1c** bytes for each of the 2 variables.
And since the variable *v5* is allocated before the *command* variable and our input is read with **scanf("%s")** we can make an overflow to write into *command* whatever we want.

The offset of *command* from *v5* is 48 since the heap alocates memory as multiples of 16 (on 64bit).
![exploit](Input_Injection_2-exploit.py)

flag: `picoCTF{us3rn4m3_2_sh3ll_e7257819}`