# mongoose

First thing I did when I opened the website was inspect the source code.
```html
      </div>
    </div>
  </div>
  <script src="/static/js/login.js"></script>
</body>
</html>
```
This poped into my eyes.

So I went on it and found this:
```javascript
const login    = document.getElementById('login');
const response = document.getElementById('response');

login.addEventListener('submit', e => {
    response.style.display = "none";
	e.preventDefault();
    console.log(new FormData(e.target));
	fetch('/api/login', {
		method: 'POST',
		body: new URLSearchParams(new FormData(e.target))
	})
        .then(resp => resp.json())
        .then(data => {
            if (data.logged) {
                login.remove();
                response.innerHTML = data.message;
                response.style.display = "block";
                window.setTimeout(function() {
                        window.location.href = '/congrats_d130ca6ea8c05c8cf7dcf76dae146f2fcfd62be082e9acb9aa2f0a5934e4eee1';
                    }, 500);
                return;
            } else {
                response.style.display = "block";
                response.innerHTML = data.message;
            }
	});
});
```

So I checked out the `/congrats_d130ca6ea8c05c8cf7dcf76dae146f2fcfd62be082e9acb9aa2f0a5934e4eee1` and saw confetti.
At first I didn't know what to do, but then I realized that the text after congrats_ looked a lot like a sha256. I wrapped it into ctf{} and send it.
It was correct.

flag: `ctf{d130ca6ea8c05c8cf7dcf76dae146f2fcfd62be082e9acb9aa2f0a5934e4eee1}`