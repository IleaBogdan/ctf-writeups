# buffer overflow 0

To get the flag we need to trigger a buffer overflow sigsegv 11.
So we need to send enough bytes that the function vuln will trigger the buffer sigsegv.

![exploit](buffer_overflow_0-exploit.py)

flag: `picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}`