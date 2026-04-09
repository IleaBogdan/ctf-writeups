# two-sum

Since in the description we have: `What two positive numbers can make this possible: n1 > n1 + n2 OR n2 > n1 + n2`
I immediately thought of integer overflow. (when A+B>INT_MAX, A<INT_MAX and B<INT_MAX)
So I send the 2 values: `int("0x7fffffff",16)` and `10` (0x7fffffff is INT_MAX)

![exploit](two-sum-exploit.py)

flag: `picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_482d8fc4}`