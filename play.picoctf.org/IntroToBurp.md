# IntroToBurp

After making a registration, I saw that it requiers a OTP code. So I captured a request in burp and decided to make a python script to brute trough all posible 4-8 OTP number combinations. But befor I could even do that I accidentally ran the script with no otp seted and got this output:
```sh
200
Welcome, bob you sucessfully bypassed the OTP request. 
Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_b3fa4f1a}
```

![[IntroToBurp-exploit.py]]

flag: `picoCTF{#0TP_Bypvss_SuCc3$S_b3fa4f1a}`