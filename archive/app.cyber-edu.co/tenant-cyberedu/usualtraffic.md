# usualtraffic

This one was a bit tricky.
The network part was simple (for me).

I opened the pcapng and looked at some requests and I saw that there is this requets type bgp that at the end had some plain text messages.
So I made a quick script to extract them.
After I extracted them and separated if they came from `10.10.10.1` or from `10.10.10.251` I saw this 2 messages:
```
Hello Router 2  !
Here is the key: 74C95604043427F0BEE1D0E16BFA53AFD537F736AD0073C4CC4E1CCB3A82B5DC
This is my secret: KQ6R50gkQLYCkY90yIBDHDznHRUyMaTijWmHO30UXjwftOMIGgZJhKh2xli7Sqln

Hello Router1!
Here is the vector: 8BF46C25D9BAD98ED8EAE6C1F7AD2D04
This is my secret: uWyYTCYqBTy9afI69to3eK0ScCA3SlPDEzBsWBnR9D8Ro7aIOqihGMPXwu/Z+HLn
```

So this is some sort of comunication that is encrypted between 2 routers.

At first I belived it is a **Vigenere Cipher** or some xor encryption or something, but I was wrong.
So I looked at hashes and RSA encryption until I found a random website that told me how to decrypt AES cipher.
I copied the functions it gave me and modified them a little to work and added them to my script.

After decoding the first secret I got a part of the flag so this was the way.

![decoder](usualtraffic-decoder.py)

flag: `CTF{25B24F21A9B698C026A7FF6D911B252414260C11A4A7F46DD6885C9BAA0A5386}`