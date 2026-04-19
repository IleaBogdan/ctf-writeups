#include<iostream>
using namespace std;

signed main(void){
    char v4[]="QeeanXKkk[ZRS]\\NBUQJ^RUL";
    long long v5[3];
    v5[0]=0x908070605040302LL;
    v5[1]=0x11100F0E0D0C0B0ALL;
    v5[2]=0x1918171615141312LL;
    char*v6=(char*)v5;
    for(int i=0;i<25;++i){
        cout<<char(v4[i]+v6[i]);
    }
    return 0;
}