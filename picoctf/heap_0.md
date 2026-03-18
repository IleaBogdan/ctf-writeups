# heap 0

This is a classic heap overflow ctf. 
When our input is read, it isn't checked it it gets outside of the allocaed area on the heap for it.
So we can simply overflow over the variable **`safe_var`** and since the variable is being checked as we try to print the flag, we can overflow with anything. 

![[heap0-exploit.py]]

flag: `picoCTF{my_first_heap_overflow_0c473fe8}`