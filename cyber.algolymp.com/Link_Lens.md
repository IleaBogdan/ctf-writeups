# Link Lens

Since we have a page that makes requests to urls we give it we need to find a way to make a request to the server on localhost. Since we need a way to make a request to localhost and there is a regex that checks for numbers or localhost we can bypass it with **localtest.me**. 
Other alternatives can be found here: https://hacktricks.wiki/en/pentesting-web/ssrf-server-side-request-forgery/url-format-bypass.html?highlight=localhost#localhost


We need to make a query to the `/register` endpoint and make an acount so we can sign it with it.
Since it checks query params from get not post we can do this:
`http://localtest.me/register?username=alex&password=mester`

```python
@app.route("/register")
def register():
    username = request.args.get("username", "").strip()
    password = request.args.get("password", "").strip()
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = password
    return jsonify({"success": True, "message": f"Account '{username}' created successfully"}), 201
@app.route("/verify")
def verify():
    username = request.args.get("username", "").strip()
    password = request.args.get("password", "").strip()
    if not username or not password:
        return jsonify({"valid": False}), 400
    if username in users and users[username] == password:
        return jsonify({"valid": True}), 200
    return jsonify({"valid": False}), 401
```

We also need to verify it so: `http://localtest.me/verify?username=alex&password=mester`

Aftr that we can simply login with the credentials we just made and we get the flag.

flag: `ALGOLYMP{3z_byp455_r1ght?}`