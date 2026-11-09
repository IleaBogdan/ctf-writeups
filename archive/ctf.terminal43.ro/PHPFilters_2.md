# PHPFilters 2

If we inspect page source we can see this block of javascript code:
```js
<script>
function sendReq() {
  var nume="username="+document.getElementById("user").value+"&message="+document.getElementById("message").value.replace("flag pls","");
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
		alert(this.responseText);
    }
  };
  xhttp.open("POST", "./check.php", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(nume);
}
</script>
```

The important part is the `.replace` function. It only replaces the first instance of `"flag pls"`. So if we pass `"flag plsflag pls"` it will send to `check.php`: `"flag pls"`

After we do that and put a random username we get an alert with the flag.

flag: `T43CTF{Javascript_Sanitization_15_n0t_th@t_s3cure}`