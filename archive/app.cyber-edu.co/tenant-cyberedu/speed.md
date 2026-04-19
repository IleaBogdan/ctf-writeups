# speed

In this ctf wee need to find out the value of v2.
It is a simple c program that sets the seed to **4548u** and then calls rand 2 times and checks some values with xor.
Since xor is reversable we can simple make this `C` code to replicate what the ctf binary does print the value of v2. After that we can simply put the result in an online sha256 calculator and we have the flag.

[[speed-exploit.c]]

flag: `CTF{0f68f60833e9872b4c58e421be66edc696584de1a573e6b985965ea2eafc46c8}`