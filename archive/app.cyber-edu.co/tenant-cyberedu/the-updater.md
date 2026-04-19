# the-updater

From this peace of code we undestand that the binary is making a GET request to a server and then reads the respons that is a key from it.
```c
write(v11, "GET /key\r\n\r\n", 12u);
memset(buffer, 0, sizeof(buffer));
while ( read(v11, buffer, 1023u) )
{
__strcpy_chk(key, buffer, 100);
v4 = strlen(key);
fprintf(__stderrp, "%s %d\n", key, v4);
memset(buffer, 0, sizeof(buffer));
}
```
If we search in the pcap for the **/key** (in the packet bytes) we find it at request 795.
We can then follow the TCP stream of the request to see the respons as well and we get this:
```python
GET /key

AAAAAA85783cc847fb84e7ba9c1c727099c9040fe086fab96857227bedc4b3967ec978
```

For the second part of the ctf, we need to take a look at this part of the code:
```c
write(v12, "GET /a.gif\r\n\r\n", 14u);
memset(buffer, 0, sizeof(buffer));
v10 = fopen("a.gif", "wb");
while ( read(v12, buffer, 1023u) )
{
fprintf(__stderrp, "%s", buffer);
fwrite(buffer, 1u, 1024u, v10);
memcpy(test, buffer, sizeof(test));
fflush(v10);
memset(buffer, 0, sizeof(buffer));
}
```
This code is the same as the other one just that it sends a request for **/a.gif**.
Doing the same as before we can find the request a index 874.
Following the TCP stream gives us this:
```python
GET /a.gif

....:x.S.Y
W....U...S.SX
TT.S.Q	.
W
RP...SY..UTZR[..WPQRU..
.UZ..PR[TE
```

So I copied the raw bytes for the 2 responses and I made a script to xor them so that we get the flag just like the binary does.
```c
printf("\nDecoded: ");
for ( i = 0; i < strlen(key); ++i )
    printf("%c", test[i] ^ (unsigned int)key[i]);
```

![solve](the-updater-solver.py)

flag: `ECSC{90f7a94e0083a95671947ead3f91444bd6abca6c46cdc18ebf00df9cfc5851bc}`