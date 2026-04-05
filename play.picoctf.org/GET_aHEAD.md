# GET aHEAD

After inspecting the source code we can see that we can send requests as get or post.
So I opened up burp and tried sendig one as puts. It worked, but nothing new.

So I remembered there is a http method named HEAD and since the ctf is named aHEAD I had the idea to send the request as a HEAD method. After that I got the flag.
```
HTTP/1.1 200 OK
Date: Sun, 05 Apr 2026 09:53:00 GMT
Server: Apache/2.4.38 (Debian)
X-Powered-By: PHP/7.2.34
flag: picoCTF{r3j3ct_th3_du4l1ty_8b13f07}
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
```

flag: `picoCTF{r3j3ct_th3_du4l1ty_8b13f07}`