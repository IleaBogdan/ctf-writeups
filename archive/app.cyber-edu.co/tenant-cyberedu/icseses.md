# icseses

The name implies XSS and then we can try doing XSS.
So looking in the source code we can see there is a bot we can trigger.

I tried some XSS, but it didn't work. After testing some other payloads we saw that we can do SSTI.
I then took a second look at the source code and saw there is a mako python server.

So I cooked a payload.
It was banned.

I looked in the mako documentation and fount that `'%c'ord(char)` in mako is the same as just `char`.
So we can change the chars of the payload to be `'%c'ord(char)`.

I made a script to replace my payloads.
![encoder](icseses-encoder.py)

I then posted the payload and hit `Show Fancy Name` and then the `Report` button.

Then in webhook I went and saw the flag.

flag: `OSC{444d1789ac974b480bf1bcb88936c4624da0c4f517e31f129fff2162bd1c98d9}`