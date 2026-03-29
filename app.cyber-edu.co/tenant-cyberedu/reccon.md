# reccon

If we do a dirb on the url we find that it has index.php.
After testing a lot of random payloads something came to my mind: `Lets brute trough params`

I know, very stupid, but I didn't even need to brute to much since if we do `/index.php?m` we get the flag.

flag: `CTF{486cdfe3a59141aca752fb10b44c70facca9c5b1d7be444aa840d14148030e66}`