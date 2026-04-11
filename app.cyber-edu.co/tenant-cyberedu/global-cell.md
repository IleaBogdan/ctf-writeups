# global-cell

At first I did a strings on the pcapng and saw the string `Paris1`.
After looking for the request with the string `Paris1` in it I found the request **2548**.
Inside this request I saw a json that has a label: *Global Cell ID discovered*
After looking inside the request a bit more I found:
```
Mobile Country Code (MCC): 208 -> This is France
Mobile Network Code (MNC): 20 -> This is Bouygues Telecom (a French mobile operator)
Location Area Code (LAC): 22510
Cell ID: 1106 (with BTS sector 69 and sector ID 2)
```

So I ran them with the opencellid api:
```sh
curl 'https://www.opencellid.org/ajax/searchCell.php?mcc=208&mnc=20&lac=22510&cell_id=1106'
```

As respons I got:
```json
{"lon":-1.03705,"lat":44.703316,"range":1000}
```
I typed them in google maps and I got a town in france named `Lanton`. (https://www.google.com/maps/place/44%C2%B042'11.9%22N+1%C2%B002'13.4%22W/@44.7064939,-1.0525888,6424m/data=!3m1!1e3!4m4!3m3!8m2!3d44.703316!4d-1.03705?entry=ttu&g_ep=EgoyMDI2MDQwOC4wIKXMDSoASAFQAw%3D%3D)

So I looked for the areacode of the town and on this website I found it is `33229`. (website: https://www.map-france.com/Lanton-33138/)

I put it into a sha256 calculator and got the flag.

flag: `ECSC{50fb4a9bee63b51141c2b32e42251d1f88104731d1a7b73ff9750626227d7f5a}`