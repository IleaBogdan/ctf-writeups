# Alice

Ok so we have 16 hashes and we are told that the attacker only queried form the first part of the hashes (I assume they ment the first 32 bytes of the 64 of a hash). 

**Part 1:** Since the hash from Alice has the values on 2 positions set and the other unseted, we can assum that the char we will find only once in the hashes is the correct hash from Alice.

**Part 2:** We can remember that a sha256 can only have hex chars (0123456789abcdef), so we can look at all the 16 hashes and see what chars they don't have in the hashes and that will be the chars Alice didn't set.

I made a simple python code to automate that:
![cracker](Alice-cracker.py)

flag: `dc0eb76143e50fe3dbeb6383605de5ffa9fefe455caca597677eab7cbf0ad649`