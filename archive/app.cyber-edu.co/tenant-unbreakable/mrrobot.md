# mrrobot

After looking at the code I realized that the only relevant part is the `sub_C81` function.
So I started reversing it.

I saw that I need a random value smaller then 16, but since our output has `01` in the begining and we have this part of the code:
```c++
v6 = rand() % 16;
if ( v6 <= 9 )
v1 = '0';
else
v1 = '1';
*v10 = v1;
v10[1] = v6 % 10 + '0';
```
We can simply find that `v6=1` is the only option.

After that everything was easy.
We can see that v5 is calculated for each char of the input and then it is used for 2 chars of the output.
With that in mind we can get v5 by checking if it is bigger or smaller then 9 and then we can simply xor it against the value of the **off_202010** (`dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv`).

I made a `C++` code that checks that for me:
![decrypt](mrrobot-decrypt.cpp)

The output of the code was: `CTF{Br3ak_th3_Cisc0_B0x}`
After I put it into a sha256 tool only I got the flag. 

flag: `ctf{17ed97dbc53e4c9bf76a20a1721be46fae380c533bf4f9a2878e201fe9d8bee9}`