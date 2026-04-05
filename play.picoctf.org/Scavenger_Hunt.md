# Scavenger Hunt

I first opened the source code of the site and saw this:
```html
<!-- Here's the first part of the flag: picoCTF{t -->
```

I also saw some file named mycss.css included in and inside it I found:
```css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```
Again in the source code of / of the website there is a file named myjs.js, inside it we have this hint:
```javascript
/* How can I keep Google from indexing my website? */
```

So I looked in robots.txt and found this:
```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```
I did a dirsearch on the website and found to pages:
First one: /.htaccess
```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```
Second one: /.DS_Store
```
Congrats! You've completed the scavenger hunt! Part 5: _9588550}
```

flag: `picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}`