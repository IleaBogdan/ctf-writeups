#include"defs.h"
#include<iostream>
#include<cstring>
using namespace std;

_BYTE * sub_1195(const char *a1)
{
  size_t v1; // rax
  _BYTE *v3; // [rsp+10h] [rbp-20h]
  int v4; // [rsp+18h] [rbp-18h]
  int i; // [rsp+1Ch] [rbp-14h]

  v1 = strlen(a1);
  v3 = (_BYTE*)malloc(v1);
  for ( i = 0; i < strlen(a1); ++i )
  {
    if ( a1[i] <= '@' || a1[i] > 'Z' )
    {
      if ( a1[i] <= '`' || a1[i] > 'z' )
      {
        if ( a1[i] <= '/' || a1[i] > '9' )
          v3[i] = a1[i];
        else
          v3[i] = (a1[i] - 35) % 10 + '0';
      }
      else                                      // 'a' <= a1[i] && a1[i] <= 'z'
      {
        v4 = a1[i] + 13;
        if ( v4 > 'z' )
          LOBYTE(v4) = a1[i] - 13;
        v3[i] = v4;
      }
    }
    else
    {
      v3[i] = a1[i] + 13;
      if ( (char)v3[i] > 'Z' )
        v3[i] -= 26;
    }
  }
  return v3;
}

signed main(){
    char s2[]="9094929R948S0N94039496920794";
    cout<<s2<<endl;
    for(int i=0;i<strlen(s2);++i){
        if(('A'<=s2[i]&&s2[i]<='Z')||('a'<=s2[i]&&s2[i]<='z')){
            // rot13
            int off=0;
            if(s2[i]<='Z'){
                s2[i]-='A';
                off='A';
            }else{
                s2[i]-='a';
                off='a';
            }
            s2[i]+=13;
            s2[i]%=26;
            s2[i]+=off;
        }else if('0'<=s2[i]&&s2[i]<='9'){
            s2[i]-='0';
            int v;
            for(v='0';v<='9';++v){
                if((v-35)%10==s2[i])break;
            }
            s2[i]=v;
        }else{
            continue;
        }
    }
    cout<<s2<<endl;
    cout<<sub_1195(s2)<<endl;
    return 0;
}