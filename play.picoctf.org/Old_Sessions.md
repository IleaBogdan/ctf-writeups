# Old Sessions

After opening the site we look at the comments on the site and we see one saying:
```
mary_jones_8992 2024-2-20 14:50
Hey I found a strange page at /sessions
```
So we go on `/sessions` and get:
```
1) session:HwYXwheueQGIdCxFm3S_KM1W_70njz1gYerWjY9h6tM, {'_permanent': True, 'key': 'admin'}

2) session:SgfvruacbpsQ0EG_tESQSJNfjdw1m93CJsKKZwiuBVU, {'_permanent': True, 'key': 'bob'}
```
We can take the session cookie that is followed by key: admin and put it in place of our cookie.
When we reload the site we get the flag. 

flag: `picoCTF{s3t_s3ss10n_3xp1rat10n5_ed8964c2}`