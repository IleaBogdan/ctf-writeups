# silent-relay

If we inspect the binary we can see that it loads the flag and then checks data from the flag to see if it is 0 or 1.
At first I belived that it is sending the flag but I was wrong. 
It is all abount the time the requests are send.
The flag is in binary (suggested by the name of the function) and if it has 0 or 1 it does a sleepp for different amount of seconds.

So I made a quick script to extract each timestamp and calculate the the difference.
Note that the requests we care abound are separated by 3 of each other and also some DNS requests are mixed among the TCP request we care about.

![script](silent-relay-solve.py)

flag: `ctf{baf9eecbff31e3d0fcdf9dc820d673594261100b0556d764800bc752d63ecdae}`