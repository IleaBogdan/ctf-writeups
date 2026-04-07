# Web10 - Chall 6

At first the `person = html.escape(request.form['name'])` hit made me think about XSS injection.
But nothing worked. 
So I turned to my trusty friend SSTI.

After some basic ssti payloads I found that it is a mako server. (`${7*7}`==49)
So since we know each char is getting html escaped we can try the `Mako CMD Execution with Obfuscation` payload tamplate from this git repo: github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server Side Template Injection/Python.md#mako

I even made a script so I can execute commands just like on my machine (50% of the time works every time).

![exploit](Web10-Chall6-exploit.py)

flag: `ALGOLYMP{m4k0...m4k0...}`