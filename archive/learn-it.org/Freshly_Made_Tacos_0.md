# Freshly_Made_Tacos_0

We have a simple format string vulerability.
I found the offset on the stack of the flag to be at 20.
After that I printed the next 10 pointers and got the flag.

![exploit](Freshly_Made_Tacos_0-exploit.py)

flag: `LearnIT{73a6e1e111e2bcd8683bbc678ec934ce4c00d8ee85721a3ccb7bc477c38cd2a6}`