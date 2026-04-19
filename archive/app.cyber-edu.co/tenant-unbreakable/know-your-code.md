# know-your-code

The first part of this ctf is simple:
```php
 <?php
require __DIR__ . '/secrets.php';
if (!isset($_GET['start'])){
    show_source(__FILE__);
    exit;
} 
function auth($username, $password, $realm='Administration') {
  if( $_SERVER['PHP_AUTH_USER'] != $username ||
    $_SERVER['PHP_AUTH_PW'] != $password ) {
    header("WWW-Authenticate: Basic realm=\"$realm\"");
    header('HTTP/1.0 401 Unauthorized');
    echo 'Access Denied';
    exit;
  }
}
auth('admin', '0password');
secret_redirect();
?>
```
We just enter the GET param `?start` and we are prompted to enter a password and a username. If we enter **admin** and **0password** just like we can see in the code we get to the next part.
```php
<?php
require __DIR__ . '/secrets.php';
if (!isset($_GET['start'])){
    show_source(__FILE__);
    exit;
} 
$password = $_GET['pass'];
//$secret_password_value is a long 64 character value that you can not guess or bruteforce!
if ($password == $secret_password_value){
    second_secret_redirect();
}
```
Here we are told to find the sectre password that is a 64 long character value. The thing that tipped me off was that it told me: `is a long 64 character value`
The idea is that it is probably a sha256 value. Since there are **16^64** possibilities so yeah we can't brute force them.
But the idea here is to look at the source code in the if. 
We see that it is checking the password with `==` so we have some room for: `type juggling`
https://hacktricks.wiki/en/files/EN-PHP-loose-comparison-Type-Juggling-OWASP%20(1).pdf
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md

So we can asume the first char of the password is 0 and it will all be considered as if it was 0. So setting the pass variable to 0 would be enough.
We can also do `0e1` but here just 0 works fine.

flag: `CTF{ba257a7449a2710c3579aa17285d36d8172af5469d7336686732dfb3615ed181}`