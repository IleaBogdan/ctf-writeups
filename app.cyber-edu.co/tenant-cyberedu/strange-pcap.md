# strange-pcap

If we open the statistics page in wireshark we see that 99.9% of the traffic is usb traffic so this pcapng is an usb capture.
Not knowing what to do I ran strings on the file and foun that inside it there is a string `Flag.txt`. 

I looked for the request that had the string and found that it is from some file that is a zip archive. I extracted the file as hex stream and decoded it in cyberchef and downloaded the archive.
When I tried unziping it I was stuck since the file needs a password.

So I got john to do the job:
```sh
zip2john download.zip > hash.txt
john hash.txt
```
However it took to much time and didn't find anything so this probably not the way.

I found this repo that tecnically extracts data from pcap files that have USB requests in them: https://github.com/shark-asmx/CTF-Usb_Keyboard_Parser 

It had an issue that gave me this error: `ValueError: 255 is not a valid URBTransferType` but after fixing it I got the password for the zip.
(my fixes can be found on my profile as a fork to the repo mentioned before)

password: `7vgj4SSL9NHVuK0D6d3F`

flag: `HackTM{88f1005c6b308c2713993af1218d8ad2ffaf3eb927a3f73dad3654dc1d00d4ae}`