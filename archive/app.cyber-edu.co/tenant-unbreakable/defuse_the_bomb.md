# defuse_the_bomb

By looking at the code I saw 2 functions we need to reverse.
The first one (`sub_1375`) just turns our input into a hex.

The second one was all over the place.
Here is a restructor of the function to be easyer to follow:
```c++
_BYTE *__fastcall sub_1195(const char *a1){
    size_t v1; // rax
    _BYTE *v3; // [rsp+10h] [rbp-20h]
    int v4; // [rsp+18h] [rbp-18h]
    int i; // [rsp+1Ch] [rbp-14h]

    v1 = strlen(a1);
    v3 = malloc(v1);
    for ( i = 0; i < strlen(a1); ++i ){
        if ( a1[i] >= 'A' && a1[i] <= 'Z' ){
            v3[i] = a1[i] + 13;
            if ( (char)v3[i] > 'Z' )
                v3[i] -= 26;
            continue;
        }
        if ( a1[i] >= 'a' && a1[i] <= 'z' ){
            v4 = a1[i] + 13;
            if ( v4 > 'z' )
                LOBYTE(v4) = a1[i] - 13;
            v3[i] = v4;
            continue;
        }
        if ( a1[i] >= '0' && a1[i] <= '9' ){
            v3[i] = (a1[i] - 35) % 10 + '0';
            continue;
        }
        v3[i] = a1[i];
    }
    return v3;
}
```

A breakdown of the functions is that it takes each char of the hexed input and then it does a rot13 on it if it is a letter and if it is a number it does some modulo operation on it.

After knowing that we can make a simple code to undo the operations and get the original hex string.
![undo-code](defuse_the_bomb_solve.cpp)

Form that I got this hex string: `6761696E615F7A61706163697461`
Decoding it from hex gave me the password: `gaina_zapacita`

I sha256 it and got the flag.

flag: `ctf{c63344dea9cdc97a00f20edca0867575292141b74021560c29c6a4429888d832}`