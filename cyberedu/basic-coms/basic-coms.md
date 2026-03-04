
So I had no idea what to do so I started running random commands.
I found interesting the fact that there where some requests he was making to itself (127.0.0.1 to 127.0.0.1).
But it was not what it got me to the solution.

The solution was simply running: 
> cat basic-coms.pcapng | tshark -r - -Y "http.request.method==GET"

(My tshark is broken and won't open files unless I do them with cat |, but you get the idea)

The output was interesting:
```
53553 52.630465106 192.168.3.122 → 93.184.216.34 HTTP 681 GET /?important=The%20content%20of%20the%20f%20l%20a%20g%20is%20ca314be22457497e81a08fc3bfdbdcd3e0e443c41b5ce9802517b2161aa5e993%20and%20respects%20the%20format HTTP/1.1 
53656 52.821762241 192.168.3.122 → 93.184.216.34 HTTP 607 GET /favicon.ico HTTP/1.1 

```
looking at the one that has `important=` I saw that it had the letters `f` `l` `a` `g` in, only divided by spaces.
So I read what the string told me and found this in the same string `ca314be22457497e81a08fc3bfdbdcd3e0e443c41b5ce9802517b2161aa5e993`

So this was the sha256 part of the flag.

Full flag: `CTF{ca314be22457497e81a08fc3bfdbdcd3e0e443c41b5ce9802517b2161aa5e993}`