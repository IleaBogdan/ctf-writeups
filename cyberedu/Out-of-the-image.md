# Out-of-the-image

The image was talking about some passwords so doing a brute force with rockyou came to my mind.

> stegcracker quals_warmup_out-of-the-image_Simple-Survey.jpg ~/Wordlists/rockyou.txt
```
** output:

StegCracker 2.1.0 - (https://github.com/Paradoxis/StegCracker)
Copyright (c) 2026 - Luke Paris (Paradoxis)

StegCracker has been retired following the release of StegSeek, which 
will blast through the rockyou.txt wordlist within 1.9 second as opposed 
to StegCracker which takes ~5 hours.

StegSeek can be found at: https://github.com/RickdeJager/stegseek

Counting lines in wordlist..
Attacking file 'quals_warmup_out-of-the-image_Simple-Survey.jpg' with wordlist '~/Wordlists/rockyou.txt'..
Successfully cracked file with password: qwertyui
Tried 3425 passwords
Your file has been written to: quals_warmup_out-of-the-image_Simple-Survey.jpg.out
qwertyui
```

So I the did this:
> steghide extract -sf quals_warmup_out-of-the-image_Simple-Survey.jpg 
> Enter passphrase: qwertyui

 And the flag was: `ECSC{8bcaac73afa8c3a40f089ce451e1a157ba734e3a34189ddfeb32a0f709dca28c}`