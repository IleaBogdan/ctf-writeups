# you-can-trust-me

After trying and failing to crack the cookie with `flask-unsign` I decided to go on the https://www.jwt.io website  since I knew that it worked better then flask-unsigned.
It gave me that the cookie format has de headers:
```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

and the payload:
```json
{
    "user": "anonymous"
}
```

After playing a little with the cookie and sending some requests in burp with a new cookie I found that when I encode this:
```json
{
    "user": "administrative"
}
```
I get the respons: `User not allowed`, that differs from the respons: `"Hello user. Since you do not have administrative privileges I guess you will have to wait here."`
Ok this might be nothing since when I encode bob as the user I get the same thing.

SO far the encoded users that the site accepts are:
 - user
 - anonymous
 - admin

After doing a dirsearch we see there is a `/docs` endpoint marked as 307.
When we access it we get a swagger menu with this message in it: **`Note to self: Admin tokens must have the is_admin key defined otherwise we will know that it is just a normal user.`**
There is also a `/openapi.json` there, but is irelevant.

After wee add the `"is_admin": true` to our payload we get the messaged missing flag.
So we add `"flag": true` as well and get the message: missing pin.

So we need to brute force the pin.
I send a request with a random pin (1111) just to see what I get when I get the wrong pin and it told me:
`"pin is not valid. (hint)use your phone pin first 4"`
So we know the pin is only 4 digits.
We can make a script to brute trough all 4 digits pins.
![pin burt](you-can-trust-me-pin-brut.py)

The pin is 7331, it takes a while until it findes it.

flag: `CTF{2965f7e9fcc77fff2bd869db984df8371845d6781edb382cc34536904207a53d}`