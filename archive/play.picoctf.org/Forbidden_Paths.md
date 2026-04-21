# Forbidden Paths

The hint for this one was in the description.
It told us: `but the website is filtering absolute file paths`
So form this one I coudl tell I need a way to get some relative paths.

This made me think that I can simply spam a bunch of `../` and get to root from the current directory.
So I tried: `../../../../../../../../../../../etc/passwd` and it worked.
From this I got the flag using: `../../../../../../../../../../../flag.txt`

flag: `picoCTF{7h3_p47h_70_5ucc355_e5fe3d4d}`