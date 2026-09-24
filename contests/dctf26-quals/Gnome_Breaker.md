# Gnome_Breaker

The challenge gives you a dumped home directory. The hint says the flag is
stored next to the wifi / login passwords, so the target is the GNOME keyring.

Every command below is copy-pasteable. Run them in the challenge folder.

---

## Step 1 — see what we got

```bash
find . -type f
```

The two interesting files:

```
./home/masquerade/.local/share/keyrings/login.keyring
./home/masquerade/.local/share/keyrings/default.keyring
```

## Step 2 — what kind of keyring is it

```bash
file home/masquerade/.local/share/keyrings/login.keyring
```

Output:

```
GNOME keyring, major version 0, minor version 0, crypto type 0 (AES),
hash type 0 (MD5), name "Login", ..., hash iterations 1603,
salt 5342644392591054172, 1 item(s)
```

So it's the **old GNOME keyring format (v0)**: AES + MD5.

## Step 3 — look at the raw bytes

```bash
xxd home/masquerade/.local/share/keyrings/login.keyring
```

First bytes:

```
00000000: 476e 6f6d 654b 6579 7269 6e67 0a0d 000a  GnomeKeyring....
```

The magic is `GnomeKeyring\n\r\0\n`, then `00 00` (version 0.0), `00` (crypto =
AES), `00` (hash = MD5). After the name/timestamps you get the two values we
actually need:

```
hash iterations = 1603
salt            = 4a24e2c4bd9f555c
```

then a `crypto_size` field and that many bytes of AES ciphertext.

## Step 4 — how the password is turned into a key

```
digest = sha256(password + salt)
repeat 1602 times: digest = sha256(digest)     # 1603 total
key = digest[0:16]
iv  = digest[16:32]
```

Then `AES-128-CBC` decrypt the ciphertext. The first 16 bytes of plaintext are
an MD5 of the rest, so you can verify a guessed password by decrypting and
comparing.

## Step 5 — crack it

The hint says the password is weak, so rockyou it is. Use the provided script:

```bash
pip install pycryptodome
python3 solve.py
```

Output:

```
[*] home/masquerade/.local/share/keyrings/login.keyring  salt=4a24e2c4bd9f555c  iterations=1603
[+] password: masquerade2k
[Flag] ECSC{C0ngrats_you_are_AGnomeFan}
```

(Or pass the wordlist explicitly: `python3 solve.py /usr/share/wordlists/rockyou.txt`)

## Step 6 — the flag

```
ECSC{C0ngrats_you_are_AGnomeFan}
```
