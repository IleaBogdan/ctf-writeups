# Local Authority

After we login and we view the page source code we can see there is a file named secure.js included.
If we open the file we can see this code:
```javascript
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

From this we can deduce the login is `admin, strongPassword098765`. After we login with this 2 we get the flag.

flag: `picoCTF{j5_15_7r4n5p4r3n7_05df90c8}`