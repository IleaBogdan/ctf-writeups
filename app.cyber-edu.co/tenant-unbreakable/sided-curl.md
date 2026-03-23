# sided-curl

If we send `https://google.com/` as input we can notice the site tries appending .png to the end of out url.
After playing a little bit with the input we find out that the side checks if google.com is in the input.
So we can send this: `http://google.com@127.0.0.1:8000/admin#` and we will see and admin login menu html.

After tring to set the username and password of the admin.php file on local host to admin (`http://google.com@127.0.0.1:8000/admin.php?username=admin&password=admin#`), I get hit by the error:
```
URL too long, stop HACKING ME

undefined
```
So I tried this: `http://google.com@0.0.0.0:8000/admin.php?username=admin&password=admin#`
Same issue. After looking a little online I find out that I can simply put: `0` in place of `127.0.0.1` (the reason why it works is because when you do http://0:port your request gets redirected to 127.0.0.1)

The valid payload: `http://google.com@0:8000/admin.php?username=admin&password=admin#`

flag: `CTF{36555d5ff86de7b5a572f4c01cbfc8c677b1c1287d9c043618442d248d940b65}`