# log-analysis1

##### Q1:
In the `PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt` file at the end we can find this command: `C:\Users\BITSEN~1\AppData\Local\Temp\Procdump\procdump64.exe -ma lsass.exe lsass.txt`

This command dumps the lsass process on the system.

flag q1: `procdump64.exe -ma lsass.exe lsass.txt`

##### Q2:
We can look at the `SystemInfo/output.txt` file and at the networdk card we find the ipv4 ip address.

flag q2: `10.0.8.16`

##### Q3:
We can open the `PhysicalDrive0_0/PowerShellHistory/Users/bitsentinel/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt` file and search for the word users. At the end of the file we see the enumerate users command.

flag q3: `net users`

##### Q4:
Googleing: `MITRE technique password os dump` gives us this webiste: https://attack.mitre.org/techniques/T1003/
From here we can get the techinque id and name.

flag q4: `T1003:OS Credential Dumping`

##### Q5:
Looking only for this one I found this website: https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx

Here I found:
```
Windows	4798 	A user's local group membership was enumerated.
Windows	4799 	A security-enabled local group membership was enumerated
```

flag q5: `4798`