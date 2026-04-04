# anti-browser


After opening the ip with nc and sending ls as input 2 times I get prompted with:
`Introdu parola din rockyou.txt:`

So I made a script in python to read rockyou and send each line as password for this ctf.

After running it I got this:
```python
b'Introdu parola din rockyou.txt: princess\r\n\r\nWell done!\r\nctf{ffb5058001b5f773065c4e3d09600302256983335a2a7ef8d4d6a14598041707}\r\n\r\n'
```
(note: if it doesnt work in the first 3 minutes ctrl+c it and rerun it.)

![exploit](anti-browser-exploit.py)

flag: `ctf{ffb5058001b5f773065c4e3d09600302256983335a2a7ef8d4d6a14598041707}`