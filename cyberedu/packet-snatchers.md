# packet-snatchers

The ctf gives us a pcap file, so I opened it in wireshark and started looking at stuff.

### q1:
I did Edit -> Find Packet and entered the string backup.sql after selecting to query for Packet bytes

q1 flag: `DCTF{Raw IPv4}`


### q2:
I applied a search filter to only look at the ftp protocols (I typed ftp in the filter textbox).
After that we can see that the first request that does *RETR employee.pdf* was request 8 and befor it we only had requets 1 and 4. They had 2 command in them so I copy-pasted the commands.

q2 flag: `DCTF{RETR credentials.csv,USER anonymous}`


### q3:
For this one I just applied the search filter as http and the first request I saw was a GET request. There I found the flag.

q3 flag: `DCTF{contracts.docx}`


### q4:
For this one I just applied the search filter as dns and the first request had a base64 string. 
I decoded the base64 string and got the flag.

q4 flag: `DCTF{credentials.csv}`

### q5:
After applying a search filter to only look at the ftp Protocols, I also did a Find Packet on the filtered packets (yes you can apply both at the same time) and saw that only 2 were downloaded. (the Find Packet filter was RETR) 

q5 flag: `DCTF{credentials.csv,employee.pdf}`

### q6:
I applied the search filter: *tcp.flags.fin == 1* and counted 12 results.

q6 flag: `12`

### q7
After running capinfos traffic.pcap in terminal, I looked at the Average packet size output and saw 67.09. I tried 67.09 but it gave me wrong answer, but after doing just 67 it was good. 

q7 flag: `67`

### q8:
```
cat traffic.pcap | tshark -r - | awk 'END{total=NR} !/^$/{dns+=/DNS/} END{printf "%.2f%%\n", dns*100/total}'
```
This command gave me the exact number that was the flag.

q8 flag: `11.6`