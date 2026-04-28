# Sherlock's Mystery

After looking around in the trace I found this command:
```sh
PS C:\Users\alice\Desktop> New-Item "C:\Users\alice\Desktop\whatyouneedishere.txt"
```

Investigating it forward I found this other command:
```sh
S C:\Users\alice\Desktop> Add-Content "C:\Users\alice\Desktop\whatyouneedishere.txt" 

"dGhpc2lzdGhlMXN0ZmxhZw=="
dGhpc2lzdGhlMXN0ZmxhZw==
```

I decoded the text from base64 and got: `thisisthe1stflag`

flag: `ctf{thisisthe1stflag}`