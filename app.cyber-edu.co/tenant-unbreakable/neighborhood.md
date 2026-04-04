# neighborhood

After reading a little about `EAPOL` and `IEEE 802.11` I found out that EAPOL is a protocol that has the purpose to be facilitate the authentication between a clien and a router. A way to crack EAPOL handshakes is using a command line tool named `airctack-ng`.

After running this command:
```sh
aircrack-ng -w ~/Wordlists/rockyou.txt neighborhood.pcap
```

I saw that the hidden password was `mickeymouse`.

Putting it in a sha256 generator gave me the flag. 

flag: `CTF{d0ff2794ec7af8764a654b31b68d07aec0f518053fee9629917a5782ad9cf837}`