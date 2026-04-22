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