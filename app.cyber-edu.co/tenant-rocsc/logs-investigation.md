# logs-investigation

In the file `PhysicalDrive0_0/PowerShellHistory/Users/attacker/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt` we can find the logs of all commands ran by users.

Q1: I tried looking for commands with password in them but they had to big of a char count. 

q1 flag: ``

Q2: I searched for the word Users in the file and found a lot of commands, however the one that stood out was the one that did not have Users as part of a file path. I then looked on google `enumerate users windows command` and got this website from microsoft: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net-user

So yeah for sure the command with net users in it was the one.

q2 flag: `net localgroup users`

Q3:
If we take a look in the `SystemInfo` folder from the unziped zip we have a file named `output.txt` and inside it we can see the ip addres.
```
Network Card(s):           1 NIC(s) Installed.
                           [01]: Intel(R) 82574L Gigabit Network Connection
                                 Connection Name: Ethernet0
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 10.0.8.34
                                 [02]: fe80::2044:1feb:98c2:a511
```
q3 flag: `10.0.8.34`

Q4: After searching for the word Desktop we find the command 2 commands, since we are on windows the one with `dir` in it is the one we care about.

q4 flag: `dir C:\Users\attacker\Desktop`