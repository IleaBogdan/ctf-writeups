# Web03 - 03: SSRF

I tried seeing if the flag would be in the request by sending the link to my webhook, no luck tho.
After trying to redirect it to localhost I can see the server is set on port 80.

I then decided to brute force trough some ports that might have interesting servers on them:
```
21, 22, 23, 25, 37, 53, 67, 68, 69, 79,  
80, 101, 110, 111, 119, 135, 137, 138, 139, 143,  
161, 179, 389, 443, 445, 465, 514, 543, 587, 993,  
1080, 1433, 1521, 1543, 1921, 2049, 3306, 3389, 8080, 9091
```

So I made this script to leak the ones that work:
![leaker](Web03-03:SSRF-leaker.py)

flag: `ALGOLYMP{ssrf_1nt3rnal_fl4g}`