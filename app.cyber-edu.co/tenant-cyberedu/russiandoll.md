# russiandoll

After running file on the file we downloaded we see it is a gzip archive.
We unzip it and then we see a zip archive.
Judging by the name of the ctf we can imagine multiple archives inside each other. 
The zip archive needs a password that we can crack with john.
So I made a simple script to extract each zip and gzip archive.
After some extractions I get hit by a 7z archive (again with a password). So I add that to the script.

After letting the script run for like a hour I get the flag.
(Probably I should have made it faster, but it was to much work at the time and I watched an episod of The Sopranos)

***Note: replace the path to where you cloned the git repo for john in the script, I had it in ~***
![cracker](russiandoll-crackhead.py)

flag: `ctf{8ffe609c04a7001a908da5b481442ce1ce3208f2a4f3a6862e144bb1f320c54e}`