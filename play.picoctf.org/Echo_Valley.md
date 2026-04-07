# Echo Valley

For this ctf we need to abuse the format string vulnerability, but first we need to leak the pie of the binary.
I check what address has the most likelihood of being a pie address and calculated an offset for it.

After I got pie I used the `fmtstr_payload` function from the python library: pwntools 
And made a payload to overwrite the pointer to the `push rbp` address from main on the stack so that main returns to our address.

![exploit](Echo_Valley-exploit.py)

flag: `picoctf{f1ckl3_f0rmat_f1asc0}`