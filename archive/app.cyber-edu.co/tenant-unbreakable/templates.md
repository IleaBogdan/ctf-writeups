# templates

After testing some values inside the `?err` query param I found that when I typed `${7*7}` I didn't get an output.
So even if I did't get an output I thought it might be and SSTI injection vulnerability.

So I took the first command in this list: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md#mako---remote-command-execution
(this to be more exact: `${self.module.cache.util.os.system("id")}`)

And I got an output.
So I executed `ls` and got that there is a file named flag. I ran `tac` on it and got the flag.

flag: `UNR{26ym3y-aqqqep-idhz4s-boxxwi-o5enrq-tpviyj-sp5wjw-dszds3}`