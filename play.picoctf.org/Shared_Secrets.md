# Shared Secrets

After understaning the algorithm that was used to encrypt the flag we see we can decrypt by just xoring the shared and the cipher text.
I made a script to do it for me.

![decode](Shared_Secrets-decode.py)

flag: `picoCTF{dh_s3cr3t_32ec2679}`