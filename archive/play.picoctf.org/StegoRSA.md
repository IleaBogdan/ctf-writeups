# StegoRSA

We can run exiftool on the the image and we will see that it has a comment that is a long hex string.
Decoding it gave told me that it was the secret key.

So I made a simple script to decoded the flag.enc content.

![decoder](StegoRSA-decoder.py)

flag: `picoCTF{rs4_k3y_1n_1mg_3a1b0454}`