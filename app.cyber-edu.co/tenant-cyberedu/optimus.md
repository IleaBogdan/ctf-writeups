# optimus

The binary has some sort of a gdb checker in place, so I can't run it in gdb to see what is hanging.
So I made a copy of the `C` code from ida in my own file.

It was still hanging and I belive because it makes a lot of recursive calls to this one specifict function: `sub_13B0`
So as any good programer would do I started looking and understanding the code.... yeah, good joke.
I saw that the function only gets a variable as an input and I remember my competitive programing years when I would do something called memoaization of this sort of stuff. (https://www.geeksforgeeks.org/dsa/what-is-memoization-a-complete-tutorial/)

After adding the simple memoaization trick it skyrocketed. Still it was slow after a while but it was working faster then nothing.
So I compiled it with the -Ofast flag.
```
g++ -Ofast optimus.cpp -o bin && ./bin
```
That made a little faster but still not enough.

I then added memoaization to the other function called in the program even if it probably wont be usefull.
After 5h of letting it run in the background I finally got the flag.
![optimus++](optimus.cpp)

I got this solver from a friend. It is much faster:
![solver](optimus-solver.py)

flag: `CTF{4fbbd4cf3a8445bc22bd3596f4e38bcf692dc5131e2b7d3543f3c9df205fc6d3}`