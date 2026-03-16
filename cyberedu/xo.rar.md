# xo.rar

The named made me think of xor, so I uploaded the file to cyberchef and then looked in the file data. 
I saw something named PK and started looking on the internet until I found that the headers for it starts with `50 4B 03 04`.
The idea was that the first bytes were null so that means they ware xor-ed with them self. 
I tried some a brute force to see hoe many bytes where in the xor key and after testing multiple xor keys I got this key: `50 4B 03 04 14 00 08 00`

When I opened the file it was empty, but I then hit alt+a and the flag revealed itself to me. 

flag: `ECSC{271254e9a1d893192ba42423a2ca98c7a520115daa3e57b6f89c9a206f5f0252}`