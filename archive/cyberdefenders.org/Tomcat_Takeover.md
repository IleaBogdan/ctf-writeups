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