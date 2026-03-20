# PIE TIME 2

This is a classic pie leak problem since we have format string vulnerability (ptrinf on our input).
We can try locating a binary address via **`%i$p`** and then find it's offset. 
After that we just send the hex of the ***win address*** + ***pie***. 

Took me some time figuring out how %lx works, but after testing with this porgram I made in `C++` I figured out that it reads hex input and converts it into a regular number.
![[test_pie_time_2.cpp]]

Exploit:
[[exploit-pie-time-2.py]]

flag: `picoCTF{p13_5h0u1dn'7_134k_9d4030a3}`