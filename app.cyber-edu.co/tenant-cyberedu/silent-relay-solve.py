from scapy.all import *

time = []
answer = ""

scapy_cap = rdpcap('exfil.pcapng')

for index in range(1,len(scapy_cap),3):
    pkt = scapy_cap[index]
    if pkt.haslayer(DNS):continue
    time.append(pkt.time)

for index in range(1,len(time)):
    prev = time[index-1]
    cur = time[index]
    diff = cur-prev
    if(diff>0.4000):
        answer+="1"
    else:
        answer+="0"

print(answer)