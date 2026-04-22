# the-code

This code blocks us from simply doing `escapeshellcmd` on our input.
https://www.php.net/manual/en/function.escapeshellcmd.php

However I found this way to bypass them: https://github.com/kacperszurek/exploits/blob/master/GitList/exploit-bypass-php-escapeshellarg-escapeshellcmd.md 

So I rand: `/?start&arg=sth -or -exec cat flag ;`
This gave me a long base64 string: `Y3RMEZM4MGEXYZAYMGM0NGYYZJI5MJNINTCYMTE1ZTK1MJK0YMI2MJJMNGRLMZI4NJRJZJNJZTNHNTI0YJQWZTU2N2R9Y3RMEZM4MGEXYZAYMGM0NGYYZJI5MJNINTCYMTE1ZTK1MJK0YMI2MJJMNGRLMZI4NJRJZJNJZTNHNTI0YJQWZTU2N2R9`

So I put it into cyberchef. And it was not all printable chars.
So after tring a python bruteforcer in all the posibilitis I saw that it was repeating itself.
So the actuall string we needed to decode was: 
`Y3RMEZM4MGEXYZAYMGM0NGYYZJI5MJNINTCYMTE1ZTK1MJK0YMI2MJJMNGRLMZI4NJRJZJNJZTNHNTI0YJQWZTU2N2R9`

Still with the script was to slow.
So while the script was running I went into cyberchef and tried to set each char to lower and see if I get printable chars from **"abcdef1234567890{}"**

After like 5 minutes I came up with: `Y3RmezM4MGExYzAyMGM0NGYyZjI5MjNiNTcyMTE1ZTk1Mjk0YmI2MjJmNGRlMzI4NjRjZjNjZTNhNTI0YjQwZTU2N2R9`

This decoded from base64 gave me the flag.

flag: `ctf{380a1c020c44f2f2923b572115e95294bb622f4de32864cf3ce3a524b40e567d}`