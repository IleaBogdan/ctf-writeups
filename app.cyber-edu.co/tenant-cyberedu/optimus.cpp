#include"defs.h"
#include<iostream>
#include<stdio.h>
using namespace std;

int dword_20C0[]={0x0A,0x14,0x1E,0x28,0x32,0x3C,0x46,0x50,0x5A,0x64,0x6E,0x78,0x82,0x8C,0x96,0x0A0,0x0AA,0x0B4,0x0BE,0x0C8,0x0D2,0x0DC,0x0E6,0x0F0,0x0FA,0x104,0x10E,0x118,0x122,0x12C,0x136,0x140,0x14A,0x154,0x15E,0x168,0x172,0x17C,0x186,0x190,0x19A,0x1A4,0x1AE,0x1B8,0x1C2,0x1CC,0x1D6,0x1E0,0x1EA,0x1F4,0x1FE,0x208,0x212,0x21C,0x226,0x230,0x23A,0x244,0x24E,0x258,0x262,0x26C,0x276,0x280,0x28A,0x294,0x29E,0x2A8,0x2B2};
int byte_2060[]={'d',0x0A8,'b',9,'<',0x80,'\\',0x0CB,'p',0x85,'|',0x0FB,'N',0x0E6,'a',0x0C0,0x0E9,0x0C5,0x91,0x8A,0x0FE,'m',0x80,0x0D6,0x9D,'T',0x90,0x87,'0','y',0x0BF,0x8C,0x86,'Y','D',0x0AF,0x9C,0x0FA,0x0D8,'A','C',0x0D7,'!',0x0A1,'4',0x0A6,'@',0x93,0x0FE,0x0EC,0x0F9,0x0EC,0x9F,0x27,'5','.',0x19,8,6,0x0DF,0x0DC,0x97,0x0A5,'W',0x0C5,0x0BB,'e',0x82,'!',0x1B, 0,0};

__int64 dp[1000001];
__int64 sub_13B0(int a1)
{
    if(dp[a1])return dp[a1];
    __int64 result; // rax
    __int64 v2; // r10
    int v3; // r8d
    int i; // r11d
    int v5; // edx
    __int64 v6; // rsi
    int j; // r9d
    int v8; // r14d
    __int64 v9; // r15
    int k; // ecx
    int v11; // r12d
    __int64 v12; // r13
    int m; // ebp
    __int64 v14; // rbx
    __int64 v15; // rax
    unsigned int v16; // eax
    __int64 v17; // rdi
    __int64 v18; // rax
    int v19; // eax
    int v20; // eax
    int v21; // eax
    __int64 v23; // [rsp+4h] [rbp-68h]
    int v24; // [rsp+10h] [rbp-5Ch]
    int v25; // [rsp+1Ch] [rbp-50h]
    int v26; // [rsp+20h] [rbp-4Ch]
    int v27; // [rsp+24h] [rbp-48h]
    int v28; // [rsp+28h] [rbp-44h]
    __int64 v29; // [rsp+2Ch] [rbp-40h]

    v29 = a1 + 2;
    result = 55;
    if ( a1 > 0 )
    {
        v2 = 1;
        v3 = 1;
        if ( a1 != 1 )
        {
            v2 = 2;
            for ( i = 2; i != a1; v2 += (v6 * v21) ^ 0x37 )
            {
                v5 = 1;
                v6 = 2;
                for ( j = 2; v5 != v3; v6 += (v9 * v20) ^ 0x37 )
                {
                v8 = 1;
                v9 = 2;
                for ( k = 2; v5 != v8; v9 += (v12 * v19) ^ 0x37 )
                {
                    v11 = 1;
                    v12 = 2;
                    for ( m = 2; v11 != v8; v12 += (v14 * v18) ^ 0x37 )
                    {
                        v14 = 1;
            LABEL_10:
                        ++v14;
                        if ( m != 2 )
                        {
                            v17 = 2;
                            while ( 1 )
                            {
                                v28 = k;
                                v27 = v3;
                                v26 = j;
                                v25 = v5;
                                v24 = i;
                                v23 = v2;
                                v15 = sub_13B0(v17);
                                v2 = v23;
                                v14 += v15;
                                i = v24;
                                v5 = v25;
                                j = v26;
                                v16 = v17 + 1;
                                v3 = v27;
                                k = v28;
                                if ( v11 == (_DWORD)v17 )
                                    break;
                                v17 = v16;
                                if ( v16 == 1 )
                                    goto LABEL_10;
                            }
                        }
                        v18 = (unsigned int)(v11 + 3);
                        v11 = m++;
                    }
                    v19 = v8 + 3;
                    v8 = k++;
                }
                v20 = v5 + 3;
                v5 = j++;
                }
                v21 = v3 + 3;
                v3 = i++;
            }
        }
        dp[a1]=(v2 * v29) ^ 0x37;
        return dp[a1];
    }
    dp[a1]=result;
    return result;
}
__int64 dp2[691];
__int64 sub_15A0(int a1){
    if(dp2[a1])return dp2[a1];
    __int64 v1; // r12
    unsigned int v3; // ebx
    __int64 v4; // rdi

    if ( a1 == 2 )
        return (2 * (a1 + 2)) ^ 0x37;
    if ( a1 > 1 )
    {
        v1 = 2;
        v3 = 2;
        while ( 1 ){
            v4 = v3++;
            v1 += sub_13B0(v4);
            if ( a1 == v3 )
                return (v1 * (a1 + 2)) ^ 0x37;
        }
    }
    return 1;
}
signed main(){
    char **a2;
    __int64 v3; // rbp
    __int64 v4; // rdi
    int v5; // ebx
    int v6; // eax
    __int64 v7; // r14
    unsigned int i; // r15d
    unsigned __int64 v9; // rax
    __int64 v10; // rdx
    char v12[72]; // [rsp+0h] [rbp-88h] BYREF
    unsigned __int64 v13; // [rsp+48h] [rbp-40h]

    v3 = 0;
    do{
        v5 = dword_20C0[v3];
        LOBYTE(v6) = 1;
        if ( v5 > 1 )
        {
            v7 = 0;
            for ( i = 0; i != v5; ++i ){
                v7 += sub_15A0(i);
            }
            v9 = v7 * (v5 + 2);
            v6 = ((v9 ^ 55) >> 56)
                ^ ((v9 ^ 55) >> 48)
                ^ ((v9 ^ 55) >> 40)
                ^ ((v9 ^ 55) >> 32)
                ^ ((v9 ^ 55) >> 24)
                ^ v9
                ^ 55
                ^ (v9 >> 16)
                ^ (v9 >> 8);
        }
        v12[v3] = byte_2060[v3] ^ v6;
        v10 = (unsigned int)v12[v3];
        a2 = (char **)"%c";
        ++v3;
        cout<<char(v10);
        fflush(stdout);
    }while(v3!=69);
    v12[69] = 0;
    cout<<v12;
    return 0;
}