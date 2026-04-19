# pyterm

After doing a nc on the ip and sending A we get and error.
So I decided to send the number 5.
I get: `exec() arg 1 must be a string, bytes or code object`
I then looked up pyterm on google and found this git repo: https://github.com/PyTermGithub/PyTerm/

In the folder main in the file engine.py we can find the function exec and we see it just executes some commands.
So we can try sending commands.

I tried ls and it was blacklisted. I tried some ls alternatives, but still no luck.

So I made a simple script to find all the blacklisted chars and some inputs I thought might be relevant checking.
```
blacklisted:
6,\,e,f,i,l,v,/bin/sh,import,self,

allowed:
!,",#,$,%,&,',(,),*,+,,,-,.,/,0,1,2,3,4,5,7,8,9,:,;,<,=,>,?,@,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,[,],^,_,`,a,b,c,d,g,h,j,k,m,n,o,p,q,r,s,t,u,w,x,y,z,{,|,},~,_,__,
```

![blacklist](pyterm-get-blacklist.py)
![exploit](pyterm-exploit.py)

flag: `CTF{c54f60751af79f92fd93a3a2f78eb2461e8ce614c879a1bb85fb1c0e32bd7ec3}`