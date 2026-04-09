# format string 1

We have a format string vulnerability that we can exploit by leaking the variables on the stack that have the flag in them.
I made a file named flag.txt and filled it with A and then looked on the stack to see what offset has 0x41414141. I found the first offset at 14, so there is where our flag will be.

![exploit](format_string_1-exploit.py)

flag: `picoCTF{4n1m41_57y13_4x4_f14g_64277116}`