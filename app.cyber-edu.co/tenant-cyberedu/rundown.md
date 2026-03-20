# rundown

I curled the site as a POST request and saved the output in a html file to view it.
It had some python errors and I coudl tell it was a python2.7 flask server.

After reading the code I saw that there is used some function named pickle and after looking it up it has some seriouse vulnerabilitys.

So I cooked an exploit:
[[rundown-exploit.py]]

flag: `ctf{e687c7f3f6ae2d8154dfae81b5caa978ffdebe42142234e06de26e61c95e3371}`