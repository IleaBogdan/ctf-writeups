# pcap-analysis1

First thing: we need to find the password for the zip file.
```sh
zip2john pcap-analysis1.zip > hash.txt
john hash.txt
```

John found that the password is `infected`.
Now we can actually get some job done.


##### Q1:
The IP address of the compromised host is found in the first request.

flag q1: `10.12.17.103`

##### Q2:
From the 6th request (the first HTTP request we can see) we will see that we have this part of the request:
```
GET /?awIY2Vu4=APYBCKsCs3LUw HTTP/1.1
Accept: text/html, application/xhtml+xml, */*
Accept-Language: en-US
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
Accept-Encoding: gzip, deflate
Host: sentinelplumbers.ca
DNT: 1
Connection: Keep-Alive
```
After some looking only I found that Windows NT 6.1 is the kernel version corresponds to Windows 7.


flag q2: `windows7`

##### Q3:
By looking in the extractable objects of the http streams we see that one is some file named: `awIY2Vu4=APYBCKsCs3LUw`
After trying it and not getting the flag I decied to look in the http request from where wireshark found it since somethimes wireshark hallucinate.
So I did and well I saw this part:
```
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 17 Dec 2018 17:05:19 GMT
Content-Type: application/msword;
Content-Length: 428032
Connection: keep-alive
X-Powered-By: PHP/5.4.45
Content-Disposition: attachment; filename=invoice_823719.xls
Pragma: private
```
So the file we are looking from is `invoice_823719.xls` since it is an attachment.

flag q3: `invoice_823719.xls`

##### Q4:
Since we need to check the file on virus total my best idea was: 
 - extract the file as a hex stream 
 - copy paste the hex stream in cyberchef and download the from hex output.
 - run sha256sum on the downloaded file and paste the sha in virustotal
VirusTotal flaged it as malware (as we knew) and then gave me 3 family labels:
 - **emooodldr**
 - **hancitor**
 - **geral**
I tried the first one and it was wrong, but the second one worked.

flag q4: `hancitor` 