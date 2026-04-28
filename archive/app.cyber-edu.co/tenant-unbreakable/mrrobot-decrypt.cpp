#include<iostream>
#include<cstring>
using namespace std;

signed main(void){
    char v10[]="013032224029145C2047711D11562831021F077A1406782B28";
    // strlen(v10)==50 -> strlen(input)==25
    char ans[100]="";
    int v6=1,v3,v5,v2,v100=0;
    char off_202010[]="dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv";
    for(int i=2;i<50;i+=2){
        v3=v10[i+1];
        v2=v6++;
        char high_char = v10[i];
        int high_nibble;
        if(high_char > '9'){
            high_nibble = high_char - '7';  // 'A'-'F' -> 10-15
        }else{
            high_nibble = high_char - '0';  // '0'-'9' -> 0-9
        }
        // Get low nibble from v10[i+1]
        char low_char = v10[i+1];
        int low_nibble;
        if(low_char > '9'){
            low_nibble = low_char - '7';
        }else{
            low_nibble = low_char - '0';
        }
        // Reconstruct v5
        int v5 = (high_nibble << 4) | low_nibble;
        ans[v100++]=char(off_202010[v2]^v5);
    }
    ans[v2]=0;
    cout<<ans<<endl;
    int v1,v8,i;
    int v9 = strlen(ans);
    if ( v9 > 25 )
        v9 = 25;
    v6 = 1;
    if ( v6 <= 9 )
        v1 = '0';
    else
        v1 = '1';
    *v10 = v1;
    v10[1] = v6 % 10 + '0';
    for ( i = 2; i <= 2 * v9; i = v8 + 1 )
    {
        v2 = v6++;
        v5 = ans[(i >> 1) - 1] ^ off_202010[v2];
        v10[i] = (v5 >> 4) + '0';
        if ( (v5 & 0xFu) > 9 )
        v3 = (v5 & 0xF) + '7';
        else
        v3 = (v5 & 0xF) + '0';
        v8 = i + 1;
        v10[v8] = v3;
    }
    v10[i] = 0;
    cout<<v10<<endl;
    return 0;
}