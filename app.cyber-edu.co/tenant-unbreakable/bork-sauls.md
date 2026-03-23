# bork-sauls

By looking at the code at first sight I didn't notice what could be a problem.
But after looking close at what the option 3 does and seeing that there is no check the value gets over int (signed int) we realize that spaming the 3 option will cause a int overflow and make the variable be negative and give us the flag.

![exploit](bork-sauls-exploit.py)

flag: `ctf{d8194ce78a6c555adae9c14fe56674e97ba1afd88609c99dcb95fc599dcbc9f5}`