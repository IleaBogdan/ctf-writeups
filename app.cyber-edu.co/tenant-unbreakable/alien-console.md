# alien-console

After opening the nc connectiona and sending 100 A I saw that I was getting some hex like input.
So naturally as any sane individual would do, I send 99 A to see if it changes (it did not). The onyl change was that there was less output.
So I managed to figure out that the amount of output the connectiob reads is 69.
So I tried sending 69 B's.
I saw that the first 2 numbers decremented. 
So I tried multiple chars as 69 repeting strings:
```C++
A -> 22
B -> 21
C -> 20
D -> 27
E -> 26
F -> 25
G -> 24
H -> 2b
I -> 2a
J -> 29
K -> 28
L -> 2f
M -> 2e
N -> 2d
O -> 2c
P -> 33
Q -> 32
R -> 31
S -> 30
T -> 37
U -> 36
V -> 35
W -> 34
X -> 3b
Y -> 3a
Z -> 39
```

I also tried sending little char and when I send `c` I saw the first number turn into `00`.
Yep so what the console was doing probably it was taking my input and subtracting it from the flag or something like that. (Since C and c were I belive 20 numbers apart just like in ascii)

So I made a simple python script to determin where is each char setted (where each char returns `00`) and the piece them together to get the flag.

![exploit](alien-console-exploit.py)

flag: `ctf{5b838db4a213b1e2c001bef7192712c5d2b69a69fe116e3b6b06ba5fa6555da0}`