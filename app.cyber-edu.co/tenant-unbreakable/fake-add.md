# fake-add

So at first in ida, by just looking at the `C` code I couldn't see noting. After clicking to see the assembly I saw that tere is a lot of code the decompiler is not showing that looks like it is calculating some data (probably the flag).

So I cpoied all the code and tried using AI to make it runnable and print me the output, but it failed.
(If you see this and want to fix the assembly code, here you go: [assembly](fake-add-assembly.asm))

The thing that worked tho, was this `C++` code:
![C++ Code](fake-add-c-code.cpp)

flag: `CTF{th1s_is_ju5T_ADD}`