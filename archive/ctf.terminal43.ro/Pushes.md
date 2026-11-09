# Pushes

So we have to push a button for 10000000 times.
I looked at the page source code and I saw this:
```js
<script>
    document.getElementById('push-button').addEventListener('click', function () {
        fetch('/increment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            document.getElementById('message').textContent = 'Pushes left: ' + data.pushes_left;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
</script>
```

After that I looked at the page cookies (since we have a cookie clicker) and saw a variable named `pushes` and decided to change it to 10000000. After that I pushed the cookie like 2-3 times and got the flag in an alert.

flag: `T43CTF{cookies_for_santa}`