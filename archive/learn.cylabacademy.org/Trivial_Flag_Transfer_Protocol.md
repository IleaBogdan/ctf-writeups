# Trivial Flag Transfer Protocol

I downloaded the files from wireshark using the *Extract Object -> TFTP* method.
I got 4 files:
```sh
-rw-r--r-- 1      113 Oct  6 12:21 instructions.txt
-rw-r--r-- 1   824518 Oct  6 12:21 picture1.bmp
-rw-r--r-- 1 36578358 Oct  6 12:21 picture2.bmp
-rw-r--r-- 1  1466574 Oct  6 12:21 picture3.bmp
-rw-r--r-- 1       59 Oct  6 12:21 plan
-rw-r--r-- 1   138310 Oct  6 12:21 program.deb
```

I opened `instructions.txt`:
```
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
```

I put it into a rot13 decryptor and got:
```
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
```

So I opened `plan`:
```
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
```

It translates to:
```
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```

So I looked at the `.deb` file with `dpkg-deb -c program.deb`.
```sh
drwxr-xr-x root/root         0 2014-10-15 03:02 ./
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/doc/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/doc/steghide/
-rw-r--r-- root/root      6066 2014-10-15 03:02 ./usr/share/doc/steghide/ABOUT-NLS.gz
-rw-r--r-- root/root      2771 2014-10-15 03:02 ./usr/share/doc/steghide/LEAME.gz
-rw-r--r-- root/root      2488 2003-09-28 18:30 ./usr/share/doc/steghide/README.gz
-rw-r--r-- root/root      1763 2014-10-15 03:01 ./usr/share/doc/steghide/changelog.Debian.gz
-rw-r--r-- root/root       215 2014-10-15 03:01 ./usr/share/doc/steghide/changelog.Debian.amd64.gz
-rw-r--r-- root/root       860 2003-10-11 12:03 ./usr/share/doc/steghide/changelog.gz
-rw-r--r-- root/root      1088 2014-10-15 03:01 ./usr/share/doc/steghide/copyright
-rw-r--r-- root/root       787 2003-05-03 15:41 ./usr/share/doc/steghide/TODO
-rw-r--r-- root/root      1957 2003-10-11 12:03 ./usr/share/doc/steghide/HISTORY
-rw-r--r-- root/root       895 2003-10-11 12:04 ./usr/share/doc/steghide/CREDITS
-rw-r--r-- root/root       598 2003-09-27 10:40 ./usr/share/doc/steghide/BUGS
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/man/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/man/man1/
-rw-r--r-- root/root      3760 2014-10-15 03:02 ./usr/share/man/man1/steghide.1.gz
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/ro/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/ro/LC_MESSAGES/
-rw-r--r-- root/root     30028 2014-10-15 03:02 ./usr/share/locale/ro/LC_MESSAGES/steghide.mo
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/fr/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/fr/LC_MESSAGES/
-rw-r--r-- root/root     30386 2014-10-15 03:02 ./usr/share/locale/fr/LC_MESSAGES/steghide.mo
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/de/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/de/LC_MESSAGES/
-rw-r--r-- root/root     30268 2014-10-15 03:02 ./usr/share/locale/de/LC_MESSAGES/steghide.mo
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/es/
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/share/locale/es/LC_MESSAGES/
-rw-r--r-- root/root     29198 2014-10-15 03:02 ./usr/share/locale/es/LC_MESSAGES/steghide.mo
drwxr-xr-x root/root         0 2014-10-15 03:02 ./usr/bin/
-rwxr-xr-x root/root    290888 2014-10-15 03:02 ./usr/bin/steghide
```


I then used `ar x program.deb` to extract the content of the `deb` file.
I got 2 `.tar.gz` files and a `debian-binary` file:
```sh
-rw-r--r-- 1     1250 Oct  6 12:43 control.tar.gz
-rw-r--r-- 1   136868 Oct  6 12:43 data.tar.xz
-rw-r--r-- 1        4 Oct  6 12:43 debian-binary
```

If I extract the `data.tar.gz` archive I get a `usr/` folder with steghide in it.

I used `steghide` on the images with the password: `DUEDILIGENCE`.
In the 3rd images it worked and I got the flag.  

flag: `academy{h1dd3n_1n_pLa1n_51GHT_18375919}`