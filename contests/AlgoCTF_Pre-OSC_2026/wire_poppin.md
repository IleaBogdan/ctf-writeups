# wire poppin

First thing we need to see is that theere are 3 types of requests.
The one that actually carries the song data is the l2cap one.

So we need a way to extract it.
After 2 days of searching I found it by searching: `l2cap pcapng github ctf`
https://github.com/CarabusIoanSebastian/l2cap2wav

After running the script I got a file named capture.sbc.
I opened it in audacity and played it. 

I found the song by using shazam.

flag: `Algolymp{can't_c_me}`