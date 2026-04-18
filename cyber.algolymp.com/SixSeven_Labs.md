# SixSeven Labs

At first look I can't find anything to work here.
But after putting the link to webhook and getting a request from the server we can imply SSRF.

So I tried getting the exact localhost port of the app but I failed.
I remembered that I can do: `file://` to include local files on linux.

So the payload was:
```javascript
<div>
   <img width="1" height="1" src="file:///etc/passwd">
</div>
```
And we can see there is a user named `lucian`.

So we can try:
```javascript
<div>
   <img width="1" height="1" src="file:///home/lucian/flag.txt">
</div>
```
But no output.

Here is where I got stuck. But then I re-read the description: `Good! This is unsolvable because I deleted the flag, oh wait, i forgot that when I wrote it I used echo...`

So we can asume we will see the command history in **.bash_history**
```javascript
<div>
   <img width="1" height="1" src="file:///home/lucian/.bash_history">
</div>
```
And yes we do.

flag: `ALGOLYMP{6767676767676767676767676767}`