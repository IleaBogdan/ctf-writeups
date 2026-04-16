# Lockdown

## Pcap Analysis

##### Q1:
Afer looking for the Most amound of packages an ip send I found that the ip 10.0.2.4 is on the top of the list.

flag q1: `10.0.2.4`

##### Q2:
https://attack.mitre.org/techniques/T1046/

We get a list of ID's. I tried all of them until I found that the right one was: `T1046`.

flag q2: `T1046`

##### Q3:

After filtering for smb2 packages I searched (with ctfl+F) for `\\`.
I found 2 equests that I believed were interesting because of the content inside them: **2629**, **2678**
The content of the 2 requests contained: `\\10.0.2.15\IPC$` and `\\10.0.2.15\Documents`  

flag q3: `\\10.0.2.15\Documents,\\10.0.2.15\IPC$`

##### Q4:
After looking at the exportable objects of the SMB reuqests we can find a file named: `shell.aspx`
After we find the request we can see the Len of the write request to be: `1015024` 

flag q4: `shell.aspx, 1015024`

##### Q5:
Looking at the request made by the hacker towards the server after he uploaded the file we can see they are targeted to the port 4443, so this is the port where he use for the reverse shell.

flag q5: `4443`


## Memory Dump Aanlysis

##### Q6:
By running: `volatility3 -f memdump.mem windows.info` we get the kernel address.

flag q6: `0xf80079213000`

##### Q7:
By using volatility3 and looking at the pstree we can find the location where the malware saves itself: `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\updatenow.exe`
The MITRE ATT&CK techinque is: ``

flag q7: ``

##### Q8:
For this one we can list the processes with: `volatility3 -f memdump.mem windows.pslist.PsList`
and look for something that didn;t have the name of a windows process. This is how I spotedL `w3wp.exe`.
Apparently it is a windows app, but on this article (https://stackify.com/w3wp-exe-iis-worker-process/) I found tthis:
```
Web applications running within Microsoft’s Internet Information Services (IIS) utilize what is known as IIS worker processes. These worker processes run as w3wp.exe, and there can be multiple per computer. It is possible to run IIS on a Windows desktop or Windows server, although it is usually only seen on Microsoft Windows Servers configured as web servers.
```
Since the w3wp is used by an IIS we can asume the attacker used it to run commands on the machine.
We can get the PID to the left of where we got the name of the process.

flag q8: `w3wp.exe, 4332`


## Malware Sample Analysis

##### Q9:
Running checksec on the binary I see this:
```sh
$ checksec --file=./updatenow.exe
Error: Not an ELF file: ./updatenow.exe: PE32 executable for MS Windows 5.01 (GUI), Intel i386, UPX compressed, 3 sections
```
From there I put GUI as the flag.

flag q9: `UPX`

##### Q10:
Since I could not decompile the binary in ida to see what it does I looked it's sha on virus total. And in the behavior category I found SMTP Communications.
It provided a link so that was probably the address the malware was connectiong to.

flag q10: `cp8nl.hyperhost.ua`