# checker

This one is a very annoying ctf. At first I belived I need to inspect it with gdb and get the password in runtime but it was doing some fork operations and some env loading and my gdb kept getting messed up. So I tried a static analysis in ida.
It had a lot of functions and I was getting lost in them.
Eventually I found this part of the code that looked like the area where my input will get captured and process:
```c
if ( dub_env_var )
    {
      if ( !strcmp(path_of_curr_dir, dub_env_var) )// if they are the same
      {
LABEL_9:
        nullsub_1();                            // this does nothing
        v7 = sub_402E60((__int64)v3);
        sub_402F20((__int64)v3);
        return v7;                              // exits with some return code (probably not 0)
      }
      strncpy(v3 + 8312, dub_env_var, 0x1000u);
      if ( !v3[12407] )
      {
        *((_DWORD *)v3 + 4126) = 1;
        __strcpy_chk(v3 + 12408, v3 + 8312, 4096);
        goto LABEL_9;
      }
      return 0xFFFFFFFFLL;
    }
```
(Yeah I named some of the variables since it was easyer to track)

The only thing that stopped me from insanity was this line of code I found:
```c
v3 = a1 + 12408;
if ( !sub_4042F0(&dword_60DC80) )
{
    sub_4023D0((unsigned int)"Failed to convert pyhome to wchar_t\n", v3, v4, v5, v6, v7);
    return 0xFFFFFFFFLL;
}
```
(it is in one of the functions, I am not sure which one, maybe sub_404380)
You know what that line means? This is a python code compiled into an exe. So we can decompile it and read it as python code. 

All we need to do is:
```sh
pyinstxtractor checker
cd checker_extracted/
```
And here I found a file named **1.pyc**.
```sh
uncompyle6 1.pyc > 1.py
```

Opening the **1.py** was like a blessing from above.
```python
username = decode(decode(decode(rot13("".join(map(str, username))))))
password = md5_to_hex(md5(str.encode(decode(decode(rot13(unquote(decode("".join(map(str, password))))))))))
print("Welcome to our checker software.")
print("We need to verify your identity in order to reveal the flag.")
test_username = input("Enter username:")
if test_username == username or True:
    test_password = input("Enter password:")
    if password == test_password:
        print("Well done the flag is: ECSC{sha256(username:password)}")
    else:
        print("I do not know you!")
else:
    print("I do not know you!")
```

We have it. This is the part that gets our input and checks it.
At first I was confident I can just do a `print(username)` and `print(password)` and get them, but no, we need to work for them.

The problem is that this code has implemented it's own way to decode base64 strings, and did it so bad that it doesn't actually decode them.
```python
def decode(base64):
    ns = []
    for ch in base64:
        if ch == "=":
            break
        try:
            ns.append(ch2n[ch])
        except:
            pass

    data = ""
    rem = len(ns) % 4
    if rem > 0:
        ns += [0] * (4 - rem)
    for i in range(0, len(ns), 4):
        b3 = ns[i] << 18 | ns[i + 1] << 12 | ns[i + 2] << 6 | ns[i + 3]
        data += chr(b3 >> 16) + chr(b3 >> 8 & 255) + chr(b3 & 255)

    if rem > 0:
        return data[:-rem]
    else:
        return data
```
This was the function that was failing. (ch2n is just a map that maps each char to a index from 0 to idk, a lot)
So I decided not to fix it and go on cyberchef to do there the operations.
Starting strings were:
```python
username="IJkJG1MTEwIAIHcuHacTq1ygLmyDHG09"
password="SDBFRkgxY1ZIS3FGWjFNZkxtQUFvTiUzRCUzRA=="
```

Applying the operations to decode each of them (exept for the `unquote`, I have no clue what that one is and it worked without it) will give us this:
```python
username="ECSC-Admin"
password="be8d1435876930d45073cad33273ade7" # after md5. before md5: H4Rdt0Guess%
```

So I put this string: `ECSC-Admin:be8d1435876930d45073cad33273ade7` in an onlyne sha256 calculator and got the sha part of the flag.

flag: `ECSC{79e17ba7189bc35bcaca6b8bcc263f8a7ed672ada400be4394fa7aad74e3af08}`