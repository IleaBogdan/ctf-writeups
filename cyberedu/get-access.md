# get-access

The ctf had a C++ compiled binary with a lot of functions.
After seeing that my input is being tested against some numbers, I found the function that encodes my input. (sub_183A)

After a short analysis of the function and googling half the stuff it calls, I cam to the conclusion that it just takes each char from the input, shifts it by 6 and then adds 1337 to it. 
So I took the number it checks my encoded input against and made a python script to decode them.

[[get-access.py]]

After running the script I got the flag: `ECSC{A790DBC5E1B9660C5A98680335D636602A97B5F81FB4360CB5A530ADBC5C588C}`
