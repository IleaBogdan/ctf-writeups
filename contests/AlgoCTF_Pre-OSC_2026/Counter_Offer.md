# Counter Offer

After testing the connection to the server and getting the ecnrypted flag I saw that by sending `A` as input I get the first chars of the flag. So the server was encoding each char one by one.
We can make a script to brute force and get the flag one char at the time.
This way we can get the flag.

![exploit](Counter_Offer-exploit.py)

(In the script I used a shorter list of chars since I asumed that the content of the flag is going to be small letters. I also kinda guessed the begining of the flag is `ALGOLYMP{`, so yeah)

flag: `ALGOLYMP{fixed_nonce_same_keystream}`