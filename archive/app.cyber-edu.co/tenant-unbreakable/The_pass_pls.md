# The_pass_pls

Since the binary just check our input in a function that iterates over a global vector and xors each number in the vector with **0xF3** we can simply make a `C++` code to decode the global vector.

```c++
#include<iostream>
signed main(){
    int vec[]={0x0B0, 0x8A, 0x91, 0x96, 0x81, 0x0B6, 0x97, 0x86, 0x88, 0x0B0,
        0x0C3, 0x9D, 0x94, 0x81, 0x0C7, 0x87, 0x80, 0x0AC, 0x8A, 0x0C3,
        0x86, 0x0AC, 0x95, 0x0C3, 0x86, 0x9D, 0x97, 0x0AC, 0x0C2, 0x87,
        0x8E, 0
    };
    for(int i=0;i<=30;++i){
        std::cout<<char(0xF3^vec[i]);
    }
    std::cout<<std::endl;
    return 0;
}
```

Adn we get the flag.

flag: `CyberEdu{C0ngr4ts_y0u_f0und_1t}`