# slightly-broken

The ctf gives us a link. Opening it just gives us an error.
After doing a dirsearch on the ctf's url I found a console tab.
On the console tab we can execute python comands.

To get the flag, we put:
> import os
> print(os.popen("cat flag.txt").read())

flag: `ECSC{672e1423c22222e4e4c87e27a443b4b72c298c84f13d3ddeb771b9458ce33f32}`