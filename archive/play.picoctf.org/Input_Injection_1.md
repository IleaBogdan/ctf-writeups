# Input Injection 1

So our input gets read in the s buffer that is 208 bytes long.
After that it is passed in the function **fun** as the first param.
IN the function **fun** the second param is copied in *dest* and the first param is copied in *v3*. 
The way *v3* and *dest* are declared is that we have 10 bytes alocated for each. 
So if we do a buffer overflow we can get to write in dest that later is the param for **system**.

![exploit](Input_Injection_1-exploit.py)

flag: `picoCTF{0v3rfl0w_c0mm4nd_3185bc8f}`