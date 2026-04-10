# forest

##### Q1:
In ida I looked for the string: `You waited too long and someone grabbed you`
since around there is probably where my input is checked.

I found this code:
```c
sub_7BC0(&ptr);
if ( v100 != 4 || (v22 = ptr, *(_DWORD *)ptr != 1701999987) )
{
v88 = &waited_to_long_ptr;
s2[0] = &dword_0 + 1;
s2[1] = 0;
v91 = &unk_3F000;
v92 = 0;
((void (__fastcall *)(_UNKNOWN ***, __int64, __int64, __int64, __int64, __int64))sub_1D200)(
    &v88,
    a2,
    v18,
    v19,
    v20,
    v21);
```

From my understaning of this code is that I have to send for bytes as input.
I did a little brute force and found that the right input is `sure`.

flag q1: `sure`

##### Q2:
After keep looking in the same function I found the ans for the first question I saw this part of code:
```
sub_8660(&v88, &unk_3F13E, 8);
if ( v88 )
{
*(_OWORD *)src = *(_OWORD *)s2;
sub_7790(&unk_3F000, 43, src, &off_4ED28, &off_4EDE0);
}
```  
In the first question our fail message was in v88 so I looked to see what is in the memory address the fucntion takes in beside v88.
```c
.rodata:000000000003F13E unk_3F13E       db  62h ; b             ; DATA XREF: sub_7D80+1FF↑o
.rodata:000000000003F13F                 db  32h ; 2
.rodata:000000000003F140                 db  74h ; t
.rodata:000000000003F141                 db  68h ; h
.rodata:000000000003F142                 db  65h ; e
.rodata:000000000003F143                 db  51h ; Q
.rodata:000000000003F144                 db  3Dh ; =
.rodata:000000000003F145                 db  3Dh ; =
```
Since we know it takes 8 as an argument as well we can think that it reads from this address this string: `b2theQ==`
So I took it and put it into cyberchef and it recomanded me to decode it from base64. The decoded string was `okay`. I tested it and it worked.

flag q2: `okay`

##### Q3:
I then scrolled down a little in the same function and saw this line of code:
```c
v88 = (_UNKNOWN **)v64;
s2[0] = v63;
memcpy(v64, v62, (size_t)v63);
s2[1] = v63;
v69 = (_BYTE *)sub_96F0(5u, 1u);
if ( !v69 )
sub_75E0(5, 1);
*(_DWORD *)v69 = 1886152040;
v69[4] = 33;
v70 = 1;
if ( v63 == &byte_5 )
v70 = (*(_DWORD *)v69 ^ *(_DWORD *)v64 | (unsigned __int8)(v69[4] ^ v64[4])) != 0;
v71 = 5;
j_free(v69);
id ( v70 )
```

Prior to this (in q1) the input was stored in the v88 variable so I saw that it does some checks based on the v64 that is also what is in v88 I tought lets see what the number 1886152040 is in ascii. So I hexed it and then decoded it from hex using cyberchef and found that it represents the word `pleh`. Since we have little endian I thought of it as a possible ans. It didn't work. However I saw that in v69 it stores at index 4 the number 33 (that is ! in ascii). So I tried `help!` and it worked.

flag q3: `help!`
