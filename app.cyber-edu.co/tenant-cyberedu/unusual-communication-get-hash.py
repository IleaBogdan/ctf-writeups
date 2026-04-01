import os

os.popen("cat captura.pcapng | tshark -r - -T fields -e ip.src -e data -e icmp > output.txt")

def filter_send(lines):
    new_lines=[]
    for line in lines:
        if "10.10.10.10" in line:continue # remove reply from 10.10.10.10 
        if line=="10.10.10.1\t\t\n":continue # remove empty rows
        new_lines.append(line)
    return new_lines
def filter_hash(lines):
    new_lines=[]
    for line in lines:
        new_lines.append(line.split("\t")[1])
    return new_lines
lines=[]
with open("output.txt","r")as file:
    lines=filter_hash(filter_send(file.readlines()))
print(lines)
print(''.join(lines))