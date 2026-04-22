# my-bank

So this is a simple race condition vulnerability.
In the chall we see in the store page there is a flag we can buy but we need money for it, a lot of money.
We can only loadn 600tBTC and for the flag we need 1337tBTC.

So I first tried doing a dirsearch to see what it does and the website froze. It didn't crash and after 5 seconds it got back.
This made me think maybe it is a race condition I can trigger to make it allow me to spam for the load money.

So I made a quick script to spam the website.
![exploit](my-bank-exploit.py)

The cookies and all that I got it from Burp after I captured the request.

flag: `HackTM{584bc4a31fdd484bba1a685ba604aa7f345b89d21cf435b45bfbd3e971689075}`