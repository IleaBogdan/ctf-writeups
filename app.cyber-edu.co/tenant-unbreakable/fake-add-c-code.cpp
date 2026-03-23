#include<iostream>
using namespace std;
signed main(){
    int var_FC=0x3C;
    int var_F8=0x7;    
    int var_F4=0x2A;
    int var_F0=0x2A;
    int var_EC=0x20;
    int var_E8=0x26;
    int var_E4=0x78;
    int var_E0=0x3;   
    int var_DC=0x5A;
    int var_D8=0x1A;
    int var_D4=0x68;
    int var_D0=0x0;   
    int var_CC=0x27;
    int var_C8=0xA; 
    int var_C4=0x64;
    int var_C0=0xF; 
    int var_BC=0x4B;
    int var_B8=0x14;
    int var_B4=0x5F;
    int var_B0=0xA; 
    int var_AC=0x64;
    int var_A8=0xF; 
    int var_A4=0x55;
    int var_A0=0xA; 
    int var_9C=0x55;
    int var_98=0x15;
    int var_94=0x55;
    int var_90=0x20;
    int var_8C=0x34;
    int var_88=0x1;   
    int var_84=0x2A;
    int var_80=0x2A;
    int var_7C=0x35;
    int var_78=0x2A;
    int var_74=0x21;
    int var_70=0x20;
    int var_6C=0x21;
    int var_68=0x23;
    int var_64=0x21;
    int var_60=0x23;
    int var_5C=0x64;
    int var_58=0x19;
    
    int var_54=var_FC+var_F8;
    int var_50=var_F4+var_F0;
    int var_4C=var_EC+var_E8;
    int var_48=var_E4+var_E0;
    int var_44=var_DC+var_D8;
    int var_40=var_D4+var_D0;
    int var_3C=var_CC+var_C8;
    int var_38=var_C4+var_C0;
    int var_34=var_BC+var_B8;
    int var_30=var_B4+var_B0;
    int var_2C=var_AC+var_A8;
    int var_28=var_A4+var_A0;
    int var_24=var_9C+var_98;
    int var_20=var_94+var_90;
    int var_1C=var_8C+var_88;
    int var_18=var_84+var_80;
    int var_14=var_7C+var_78;
    int var_10=var_74+var_70;
    int var_C=var_6C+var_68;
    int var_8=var_64+var_60;
    int var_4=var_5C+var_58;
    
    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c",
        var_54,var_50,var_4C,var_48,var_44,var_40,var_3C,var_38,var_34,var_30,
        var_2C,var_28,var_24,var_20,var_1C,var_18,var_14,var_10,var_C,var_8,var_4
    );
    
    return 0;
}