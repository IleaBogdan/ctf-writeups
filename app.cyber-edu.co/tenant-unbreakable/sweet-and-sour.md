# sweet-and-sour

After tring to decode the cookie from base64 we get: "Try Harder!".
So I dirsearched the url and only got the `/dashboard`.
In burp we find out that there is a Werkzeug/2.0.3 Python/3.6.9 server, but no relevant CVEs for it are out there.

After taking a second look at the cookie we realize it's a pickle cookie.
So I made a exploit to get reverse shell.

!(exploit)[sweet-and-sour-exploit.py]

After copy pasting the cookie we get after running the script into the cookie and reload the page we get shell.
(we need to open a nc coppnection and then expose it with bore)

flag: `CTF{ccc1ccef217ed19c492bdada049ad2b0fbf1adcb72a92f13ab153aae068f797f}`