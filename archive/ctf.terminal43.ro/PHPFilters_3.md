# PHPFilters 3

We have this php code:
```php
<?php     
    include('flag.php');
    if(isset($_POST['username'])){
        if(isset($_POST['message'])){
            $aux = $_POST['message'];
            $aux = str_replace("flag","",$aux);
            $aux = str_replace("flag","",$aux);
            $aux = str_replace("flag","",$aux);
            if($aux === "flag"){
                echo $flag;
            }
        }
    
    }
?>
```

In this code we have 3 `str_replace` so if we try to concatenate a flag each time (for 3 times) we will have it replaced by "".
So my payload was simple:
```php
$aux = "fffflaglaglaglag";
$aux = str_replace("flag","",$aux);
echo $aux; # ffflaglaglag
$aux = str_replace("flag","",$aux);
echo $aux; # fflaglag 
$aux = str_replace("flag","",$aux);
echo $aux; # flag
```

After that we can get the flag in an alert.

flag: `T43CTF{R3placement_Sanitization_n3v3r_w0rks}`