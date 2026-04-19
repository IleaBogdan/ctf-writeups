# pcap-analysis2

##### Q1:
We can run: 
```sh
strings pcap-analysis2.pcapng | head 
```
The output will look like this:
```
Intel(R) Xeon(R) CPU E5-2667 v3 @ 3.20GHz (with SSE4.2)
Linux 5.13.0-35-generic
Dumpcap (Wireshark) 3.2.3 (Git v3.2.3 packaged as 3.2.3-1)
ens160
Linux 5.13.0-35-generic
s3	amazonaws
s3	amazonaws
s3	amazonaws
ns-1579	awsdns-05
awsdns-hostmaster
```
Since they are asking for network interface we need to fint the NIC (Network Interface Controller) that happens to be `ens160`. (it is the 4 row in the strings output)

flag q1: `ens160`

##### Q2:
If we look at the protocol hierarchy in the Statistics tab we see that 99% of them are TCP. Since we know that HTTP is build out of a bunch of TCP's we can assume that the malware will be in `File -> Export Objects -> HTTP`. And it was.
The first object we can export is a file named: `CalypsoAPT_win_samp.zip` 
Doing a sha256sum on it we get the flag.

flag q2: `087a9bdbf11e03ba31c983155287e6c178643967dfe20f4cd672833f900da5b1`

##### Q3:
I uploaded the sha on virustotal and got that 1/64 flag it as malware. So that was no help since it didn't tell me to much about it.
So I looked online for CalypsoAPT and found out it was was first discovered in the wild by the PT Expert Security Center in March 2019.

flag q3: `03-2019-pt-expert-security-center`

##### Q4:
Googleing the malware name gave me this webiste: https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Calypso
From there I saw a link to the security report: https://global.ptsecurity.com/en/research/analytics/calypso-apt-2019/
Scrolling a little I saw this paragraph:
```
On compromised computers, the group stored malware and utilities in either C:\RECYCLER or C:\ProgramData. The first option was used only on computers with Windows XP or Windows Server 2003 with NTFS on drive C.
```

flag q4: `C:\RECYCLER`