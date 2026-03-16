# flag-is-hidden

Since this is a steg chall aswell I started looking for images. Or some sort of files that would make it a steg chall.
I ran jadx on the apk file and then did a find for any files that end in png or jpg.

The only result was: `resources/res/drawable-v24/splash.jpg`
After copying the file in the current directory I tried decoding it. 
Comand to decode what was secrete inside of the .jpg file:
```sh
steghide extract -sf ./splash.jpg -p $(stegcracker splash.jpg ~/Wordlists/rockyou.txt)
```

After that I got this long string inside of secret.txt
*`fla................................................GGGGGG{RUNTQ3thM2NmYzdmNGY4MTJjYzRiNTExZjZkZTRkYzE1MDQyMmY0OWU4MTdjMGY2MTMyMTg1MmE4MWU2YjVmMzk2MWJhfQ==}`*

After taking what was inside of the `{}` and puting it in cyberchef to decode it from base64 I got the flag.

flag: `ECSC{a3cfc7f4f812cc4b511f6de4dc150422f49e817c0f61321852a81e6b5f3961ba}`