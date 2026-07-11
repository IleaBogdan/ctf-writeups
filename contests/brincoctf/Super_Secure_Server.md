# Super Secure Server

Looking at the source code I saw this code part:
```js
let leakedUser = "";
let leakedPass = "";

fetch('/api/config')
    .then(res => res.json())
    .then(data => {
        leakedUser = data.username; 
        leakedPass = data.password;
    });

document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const u = document.getElementById('username').value;
    const p = document.getElementById('password').value;
    const msgBox = document.getElementById('messageBox');

    // client-side password comparison
    if (u === leakedUser && p === leakedPass) {
        fetch('/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ authenticated: true })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect;
            }
        });
    } else {
        msgBox.innerText = "Incorrect username or password!";
    }
});
```

Doing a curl on the `/api/config` endpoint I get a password and a username.
Entering them I get the flag.


flag: `bronco{d0nt_3xp0se_p@ssw0rd5!}`