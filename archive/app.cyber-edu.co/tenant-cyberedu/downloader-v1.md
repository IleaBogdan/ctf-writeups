# downloader-v1

After trying to put example.com/image.png we see that the website just puts our input in a wget we can research wget and find this that wget can have the parameter  -i  to read files and do a wget of what is in the file (or this is what I understood). In our case it will throw an error (by printing that it couldn't rezolve what was in the file) and that will give us the content of the file.

(https://linux.die.net/man/1/wget)

We also see that the server has a filter for .php.
After some trial and error and checking what chars are getting a `\` before them I found out you can put  'p' and it will work just fine.

So we can send this payload:
```
http://example.com/image.png -i flag.ph'p'
```

flag: `DCTF{6789af26f90396678909a99bf46ba3a78b2f1b349fbc4385e6c50556c1d0c9ff}`
