# mlue

##### Q1:

After looking around I found to requests that look like the output to the **ps** command: **1407** and **1409**
I couldn't find anything in request **1407** that could be the flag, but in **1409** I found this line:
```
darius    177717  0.0  0.0   2684  1384 pts/2    S+   12:55   0:00 ./mblue-lockerV1
```
So the ctf name (mlue) hinted me that it might be the malware or something like that and finding the word mblue sounds to much like the ctf name.
I tried it and it worked.

flag q1: `mblue-lockerV1`

##### Q2:

After finding the request that has the output to a **ps** command I thought that `hey, maybe the ip address and port of the server is the ip address and port of the receiver of the request since the attacker is running commands on the server or something`.
And yeah, it was. 

flag q2: `127.0.0.1:9001`

##### Q3:

This is not the intended solution, but I googled linux 2 letters commands and tried out some of them until I got `ps`.
And now I found in the request with the number 1407 something that looks like the output of a ps command.

flag q3: `ps`