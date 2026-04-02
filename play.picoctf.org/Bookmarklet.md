# Bookmarklet

We can see a bookmark apearing when we open source code and we see:
```
javascript:(function() {
    var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÉÕËÆÒÇÚËí";
    var key = "picoctf";
    var decryptedFlag = "";
    for (var i = 0; i < encryptedFlag.length; i++) {
        decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
    }
    alert(decryptedFlag);
})();
```

When I ran the code it gave me the wrong flag.
So I looked at the hints and found this:
```
What happens when you click a bookmarklet?
```

So I clicked on the bookmarklet.
It pasted the code to my clipboard.

So I put the code in a file and executed it.
[decoder](Bookmarklet-decoder.js)

flag: `picoCTF{p@g3_turn3r_cebccdfe}`