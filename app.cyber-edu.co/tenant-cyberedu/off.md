# off

This ctf at first looks hard, very hard.
But after I did a little reseach on how fork works and some testing on how it will work in this context I found that I will get one procces that will execute and after I break it I will be redirected to the other one. 
The ctf has canary (my biggest enemy), but we can leak it very easlly (not %p but in a much funnier way). If we take a look in the function that reads the input we can see that it reads until we send it the char `\n`. So if we would send it 1033 bytes we would overwrite over the first byte of the canary.
Knowing that and the fact that the first byte of the canary is `\x00` we can leak the canary by writing 1032 A's and a B over the first byte of the canary and then it will be printed in the puts function that does puts(s1). Since puts wont find a `\0` char in s1 it will print past it and even print v2 that has the canary. 
So we have a canary leak now.

It will give us stack smashing but we don't care since we have a forked procces with the same canary and everything just a different PID.

And now this is a simple leak libc and make a call to system("/bin/sh") ctf.

![exploit](off-exploit.py)

flag: `ECSC{5c4f178bc7e2880a36db0ddccbe018ef0683883528af43db2458b0d6a3790596}`