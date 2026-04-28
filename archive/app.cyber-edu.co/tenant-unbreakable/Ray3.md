# Ray3

Before we start we need to asume that the env variable will be yeyy since we only know the first 4 chars from it.
After that I made a `C++` source code to reverse the function that checks our input.
```C++
#include<iostream>
#include<cstring>
using namespace std;

signed main(){
    int v7=0;
    for(auto i:"yeyy"){
        v7+=i;
    }
    v7/=30;
    char enc[]="Dd|oli|QlP|ewj}~f";
    for(int i=0;i<strlen(enc);++i){
        enc[i]^=v7;
        if(i%2)enc[i]+=4;
        else enc[i]-=4;
    }
    cout<<enc<<endl;
    // cout<<check("yeyy",enc)<<endl;
    return 0;
}
```

This gave me the string: `Good_job_continue`

flag: `CTF{62745be9d3888d69b35b0f80ec06c91e4d30ac5c42a2e18b0ee467108018f45e}`