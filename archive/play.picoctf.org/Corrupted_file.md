# Corrupted file

If we look at the file header we see the file as a JFIF file.
However the issue is that the forst 4 bytes are not the JPEG magic format (`FF D8 FF E0`).
So we need to change that. (JFIF is a subtype of JPEG or something like that)

```sh
(printf '\xff\xd8' && tail -c +3 file) > repair.jpg
```

Now we can open the repair.jpg file and we have the flag.

flag: `picoCTF{r3st0r1ng_th3_by73s_684e09bc}`