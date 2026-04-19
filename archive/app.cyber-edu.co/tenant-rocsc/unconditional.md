# unconditional

At first this looks complicated, but if we look at some of the operations it checks it simply does:
```c
v4[some_index]==some_value
```

So we can simply take all of the indexes it does that do and set them like that. Doing so we gen around 70% of the flag.
The rest we can calculate if we observe there is also another simple operation:
```c
v4[some_index_1]-v4[some_index_2]==some_value
OR
v4[some_index_1]+v4[some_index_2]==some_value
```

Doing so we can get that **v4** shoul look something like this:
```c
const char v4[]={
    67,84,70,123,89, 
    111,117,45,107,110,
    111,119,45,121,111,
    117,45,103,111,116,
    45,109,101,45,97,
    102,116,101,114,45, 
    121,111,117,45,115, 
    104,97,50,53,54,
    45,109,101,125
};
```

If we simply run a `printf` on the **v4** value we get: `CTF{You-know-you-got-me-after-you-sha256-me}`
(Note v4 does not look like this if you simply do the operations since it has like 2 non ascii printable chars inside but I replaced them to the nearest match so we I get some sens making words)

After we sha the message (from { to }) we get the flag.

flag: `CTF{e60100e9b047ca672947fdae0f114b3b052d33955c81b6df767843a4ffde439e}`