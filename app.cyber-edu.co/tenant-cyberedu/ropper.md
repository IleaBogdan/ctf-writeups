# ropper

At first, by just looking at the decompiled code in ida we see that it takes some input sizes and stuff like that when it does gets. But if we remember that gets only gets the buffer where to read we realize that the input size it takes it's just something that ida put there and it is wrong. So we have overflow.

The binary does not have pie so we can easily do ROPgadget on it to find some offsets.
We use puts to leak a libc address and then we put the libc address in libc.rip and get this:
[[ropper_img1.png]]

After I tried some of them to fine the right offset for system and binsh I got shell.

script:
[[ropper_pwn_exploit.py]]


flag: `ECSC{8da38ecba19d8c0a81e4aabbaeba7d50443eb7847f93087ec1d2a0bdf662f2c1}`