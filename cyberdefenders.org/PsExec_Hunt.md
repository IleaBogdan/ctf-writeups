# PsExec Hunt

##### Q1:
We can first find this address in request 126.
The ip address has a high volume of traffic.

flag q1: `10.0.0.130`

##### Q2:
In request 131 we first encounter a hostname that has the `-` char inside it.

flag q2: `SALES-PC`

###### Q3:
By applying the `ntlmssp.auth.username` search filter we can extract the NTLMSSP Authenticate message. The filter also highlights the user.

flag q3: `ssales`

##### Q4: 
After searching with `ctrl+F` for a file with the `.exe` (since we know it has to be an executable service) we find `PSEXESCV.exe`.
On github I found this: (https://github.com/psexsrv/PsExec)
```
PsExec is a command-line utility for executing processes on local or remote Windows systems without requiring an interactive Remote Desktop session.
```

flag q4: `PSEXESVC.exe`

##### Q5:
In the SMB traffic we focus on request that have admin paths since that is what PSExec commonly uses.
So I applyed a display filter of: `smb2` and then I `ctrl+F` for the word admin.
I found one request from the hacker to `10.0.0.133\ADMIN$`.
So the flag was admin$

flag q5: `admin$`

##### Q6:
We can analyse the smb tree by using: `tcp.stream eq 24`
By looking in the early requests we can see the attacker used in request 134 the IPC$ share, short for Inter-Process Communication.
It is a special share on Windows.

flag q6: `IPC$`

##### Q7:
If we filter for `smb` traffic not `smb2` we can see the attacker is attemplting to connect to mutliple machines, but the one we actually care about is the one with a longer names so `MARKETING-PC` poped in front of my eyes.

flag q7: `MARKETING-PC`