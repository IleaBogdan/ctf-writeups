# n4twork urg3nt investigation

After we see the word pikachu we see the languages is pikalang. https://www.dcode.fr/pikalang-language
We can decode each question.

#### Q1: 
1. What is the esoteric programming language used by the attacker?

##### q1 Ans:
For this one I tried pikalang and it worked.

q1 flag: `pikalang`

#### Q2:
2. What is the name of the tool used by the security analyst?

##### q2 Ans:
The question is stupid, but it referse to the program used to capture the pcap.

q2 flag: `networkminer`

#### Q3:
3.  What is the IP of hte Linux compromised machine?

##### q3 Ans:
Since we know the attacker made a pizza order from the compromised machine (q4), I just took the requesters ip from the same request and that was the flag.

q3 flag: `10.20.230.192`

#### Q4:
4.  We know that the attacker also ordered a pizza from the compromised host. 
Can you please tell us the place, we want to contact them, maybe they can give us the necessary files? 

##### q4 Ans:
I looked to find a packate that had the word pizza in it and found one that had the pizzzahut website.

q4 flag: `www.pizzahut.ro`