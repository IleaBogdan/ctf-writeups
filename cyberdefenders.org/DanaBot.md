# DanaBot

#### Q1:
Looking in the file we see in ther 3rd requets 2 ips. The second one is our flag.
flag: `62.173.142.148`

#### Q2:
Looking in the first requests the request with the number 8 had the string filename in it. After following the tcp stream I saw this: allegato_708.js
flag: `allegato_708.js`

#### Q3:
After coping the data from the file (it was javascript so the ascii chars directly) into cyberchef and doing a sha256 on it I got the flag.
I needed to remove the `0` at the end and the `15b6` before the function declaration to get the right hash.
flag: `847b4ad90b1daba2d9117a8e05776f3f902dda593fb1252289538acf476c4268`

#### Q4:
After putting the javascript code in a deobfuscator(this one https://obf-io.deobfuscate.io/, the other ones didn't find what I needed) and I saw this:
```javascript
var _0x1e16b0 = WScript.CreateObject("Wscript.Shell");
_0x1e16b0.Run("rundll32.exe /B " + _0x44bdd9 + ",start", 0x0, true);
```
After testing a little bit with some random flags that came from the 2 files in the javascript code I got the flag.
flag: `Wscript.exe`

#### Q5:
After looking in `File -> Export Objects -> Http` I sa there was a dll file that looked strange to me (it was strange that it was a dll).
So I put .dll as the flag and it worked.
flag: `.dll`

#### Q6:
I downloaded the dll file and applied the md5sum command on it and got the flag.
flag: `e758e07113016aca55d9eda2b0ffeebe`