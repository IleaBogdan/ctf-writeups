# GATEKEEP
## Reverse Engineering (rev)

I don't know what I did. It was 11 PM and none of us had slept since yesterday. 
Tudor drew something for me with colors (I'm colorblind btw). 
Then I translated the schematic into python code and used it to determine possible values for each character, based on the following equations:

```
(c1 + c4) ^ (c1 - c4) = 0x60
(c1 + c2 + c3) | ((c1 + c4) & (c2 & c1)) = 0x45
((c9 ^ c6) - (c8 & c6)) + (c9 - !(c1 & c2)) = 0xaf
(c7 & !c4) ^ (c1 + c5) = 0xbb
c9 + c5 = 0xa5
c9 ^ c5 = 0x41
((c6 & c5) ^ (c9 | c5)) ^ (!c5 & !c6) = 0xb2
c1 + c5 - c9 = 0x87
(c4 & c5 & c9) | ((c1 & c8 & c2) ^ (c2 + c8)) = 0xfd 
```

![alt text](gatekeep.png)

So here is the code that solved this:
```python
pos="`1234567890-=qwertyuiop[]asdfghjkl;'\\zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:\"|>ZXCVBNM<>? "
# pos="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
ans_c5_c9=[]
for i in pos:
    for j in pos:
        if ord(i)+ord(j)==0xa5 and ord(i)^ord(j)==0x41:
            ans_c5_c9.append([i,j])
ans_c1=[]
for ans in ans_c5_c9:
    c5=ans[0]
    c9=ans[1]
    c1=chr(0x87-ord(c5)+ord(c9))
    if c1 in pos:
        ans_c1.append(c1)
ans_c1=list(set(ans_c1))
ans_c4=[]
for ans in ans_c1:
    for i in pos:
        if (ord(ans)+ord(i))^(ord(ans)-ord(i))==0x60:
            ans_c4.append(i)
        if (ord(ans)+ord(i))^(ord(i)-ord(ans))==0x60:
            ans_c4.append(i)
ans_c4=list(set(ans_c4))
ans_c7=[]
for c1 in ans_c1:
    for c5c9 in ans_c5_c9:
        c5=c5c9[0]
        for c4 in ans_c4:
            for i in pos:
                if ((ord(i) & (~ord(c4) & 0xFF)) ^ (ord(c1) + ord(c5))) == 0xbb:                    
                    ans_c7.append(i)
ans_c7=list(set(ans_c7))
ans_c6=[]
for ans in ans_c5_c9:
    c5=ans[0]
    c9=ans[1]
    for i in pos:
        if (((ord(i) & ord(c5)) ^ (ord(c9) | ord(c5)) ^ ((~ord(c5) & 0xFF) & (~ord(i) & 0xFF)))) == 0xb2:            
            ans_c6.append(i)
ans_c6=list(set(ans_c6))
x="47797f54b0f9f4b5b46463e7f86655d5"
import hashlib
for c3 in pos:
    for c1 in ans_c1:
        for c2 in pos:
            for c8 in pos:
                for c4 in ans_c4:
                    for c5c9 in ans_c5_c9:
                        c5=c5c9[0]
                        c9=c5c9[1]
                        for c6 in ans_c6:
                            for c7 in ans_c7:
                                password=c1+c2+c3+c4+c5+c6+c7+c8+c9
                                ans=hashlib.md5(password.encode()).hexdigest()
                                if ans==x:
                                    print(password)
```

(Solved by Bogdan and Tudor while Matei was playing Apex Legends)