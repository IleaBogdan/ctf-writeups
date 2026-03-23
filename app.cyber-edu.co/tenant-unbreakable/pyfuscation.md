# pyfuscation

After decompiling the .pyc file with this command:
```shell
uncompyle6 chall.cpython-36.pyc > main.py
```

I get a python file that has some strange functions.

just running the file and printing all variables, I get some flag that follows the format but it is wrong.
The important function here is this one:
```python
def crazy_lol():
    if "aaaaaaaaaaaaaaaaaaaa" is "aaaaaaaaaaaaaaaaaaaa":
        if "a" * 21 is "aaaaaaaaaaaaaaaaaaaaa":
            return "yuli"
        else:
            return "w3y"
    else:
        return "opl"
``` 

By looking at it, we see that it is returning yuli, but it is a wrong syntax.
After trying all the 3 inputs the one that worked was `w3y`.

flag: `CTF{b5858f16d9e3174a367ad5beecb171dcd8e2494d6edcc7a8caa7be2082a2a31f}`