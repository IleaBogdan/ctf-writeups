# tractor

We get a file named `tractor.exe`. After looking at the file signature we get this: `4d5a 9000`. I tried executing it in a windows vm, but got no output. So I decided to look at it in ida. The main function was not doing anything and no calls to any functions were made.
However I saw a function that didn't look like a random string of chars in there: `get_key()`

After looking at the `get_key` function we can see this:
```c
void get_key()
{
    void *v0; // rsp
    char v1; // [rsp+20h] [rbp-60h] BYREF
    int v2; // [rsp+2Ch] [rbp-54h]
    char *v3; // [rsp+30h] [rbp-50h]
    __int64 v4; // [rsp+38h] [rbp-48h]
    int v5; // [rsp+40h] [rbp-40h]
    int v6; // [rsp+44h] [rbp-3Ch]
    FILE *Stream; // [rsp+48h] [rbp-38h]
    void *Buffer; // [rsp+50h] [rbp-30h]
    int i; // [rsp+58h] [rbp-28h]
    int j; // [rsp+5Ch] [rbp-24h]

    Buffer = malloc_0(0x336Du);
    Stream = fopen_0("tractor.png", "rb");
    v6 = fread_0(Buffer, 1u, 0x336Du, Stream);
    for ( i = 0; i < v6; ++i )
    printf_0("%x\n", *((char *)Buffer + i));
    v5 = 92;
    v4 = 92;
    v0 = alloca(96);
    v3 = &v1;
    v2 = 8999;
    for ( j = 8999; j < v2 + v5; ++j )
    v3[j - v2] = *((_BYTE *)Buffer + j + v5) ^ *((_BYTE *)Buffer + j);
    free(Buffer);
}
```
It looks like it reads data from the png file we also got and then computes some v3 char string. 
So I copied the function and made a small program to call it. (I also added the malloc to v3 since we would have hade an overflow otherwise)
Final function:
```c
#include"defs.h" // ida defines: https://gist.github.com/Dliv3/d011325312292182a9674797761d2b41
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
void get_key(){
    void *v0;
    char v1; 
    int v2;
    char *v3;
    __int64 v4;
    int v5;
    int v6; 
    FILE *Stream;
    void *Buffer;
    int i; 
    int j; 

    Buffer = malloc(13165);
    Stream = fopen("tractor.png", "rb");
    v6 = fread(Buffer, 1u, 13165, Stream);
    for ( i = 0; i < v6; ++i )
        printf("%x\n", *((char *)Buffer + i));
    v5 = 92;
    v4 = 92;
    v0 = alloca(96);
    v3 = &v1;
    v2 = 8999;
    v3=(char*)malloc(13165);
    for ( j = 8999; j < v2 + v5; ++j ){
        printf("%d",j);
        v3[j - v2] = *((_BYTE *)Buffer + j + v5) ^ *((_BYTE *)Buffer + j);
    }
    printf("%s",v3);
    free(Buffer);
}
int main(){
    get_key();
    return 0;
}
```

After runing my program (with g++ since gcc didn't know what alloca was) we get this output:
```
89999000900190029003900490059006900790089009901090119012901390149015901690179018901990209021902290239024902590269027902890299030903190329033903490359036903790389039904090419042904390449045904690479048904990509051905290539054905590569057905890599060906190629063906490659066906790689069907090719072907390749075907690779078907990809081908290839084908590869087908890899090The key is ea5143c3c93e8e8a359eeedf9da0b130 and the algorithm is AES128. Happy searching! :)
```
Also the ctf gives us the tag and nonce (iv) for the AES128. (Btw the algorithm is not simply AES128 it is: aes-gcm-128)

I tried decoding the string that was before the key beliving that might be the cipher text, but no, it wasn't. 
So I tried a new approach (after getting some outside help).

Maybe the flag was not in there but is still in the image, since we only xor the bytes from the image after 8999.
After tring that I got the flag.

![script](tractor-decoder.py)

flag: `CTF{406aabe5171f94b0d980571f5ae9d8be9d9436d85b64b1aea32080e3b1823664}`