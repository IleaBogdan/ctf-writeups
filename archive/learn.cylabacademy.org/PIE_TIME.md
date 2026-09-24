# PIE TIME

The ctf requiers us to give it the address of a `win` function.
The binary has something known as **PIE**. But the flaw is that it leaks the main address.
From there we can calculate the offset of the binaries **PIE**.

With the binaries **PIE** we can calculate the win function offset and send the address to the binary to get the flag.

flag: `academy{b4s1c_p051t10n_1nd3p3nd3nc3_74a2b73e}`