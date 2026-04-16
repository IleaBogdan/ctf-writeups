# the-restaurant

After selectinf all checkboxes I get a part of the flag: `CTF{192145131`

After inspecting how the request is made in burp we see that the checkboxes are send as:
```
saline-soup=on&eggless-eggs=on&mouldy-muffin=on&flag=on&order=
```
The part that we are interested in is that we have a filed named flag and we need to do: `flag=on`

After doing the same in part to we get the second part of the flag: `b9d4a78730396`

On the third part we don't have checkboxes but I belived that it will work the same, I just put `flag=on&order=` and got the flag part: `3496e2e6ff438`

On the 4th part we didn't get the flag when we put the order but we got some ticket: `ticket:wonky-wellington:funky-fondue:strawberry-sundae`

After looking at the url we see that the file is `/level2.php`. If we trie to replace the 2 with a 3 we get a new page.
After puting a name on the page an trying the flag=on trick we get nothing.
But the second page also requested a ticket so I tried putting the ticket from level2. 
I got hit with:  `Naughty naughty! Don't change your ticket!`

Same if I would send an empty ticket.

After some testing we can find that we can send:
```
order=ticket%3Aflag
```
On the level2.php when it is asking like we need the order ticket. 
4th part of the flag: `790db98b85df8`

5th patr of the flag we can observe that it takes the name and makes a signature and a delimiter for it. So if we send: test:flag it is going to make a signature for it. So sending the signature for it we get the last part of the flag: `47c9b0e2ef0a5a07}` 

flag: `CTF{192145131b9d4a787303963496e2e6ff438790db98b85df847c9b0e2ef0a5a07}`