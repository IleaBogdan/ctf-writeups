# Includes

So if we look at the page source code we see 2 files being included in. Since the ctf is named Includes I imagined it might have something to do with them.
So I looked into them and found this:
```css
body {
  background-color: lightblue;
}
/*  picoCTF{1nclu51v17y_1of2_  */
```
```javascript
function greetings()
{
  alert("This code is in a separate file!");
}
//  f7w_2of2_6edef411}
```

So yeah I got the flag from this.

flag: `picoCTF{1nclu51v17y_1of2_f7w_2of2_6edef411}`