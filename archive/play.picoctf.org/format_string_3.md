# format string 3

Ok so this one is harder then format string 1 or 2, or you might thinks so, but no. The ctf is simple because we have the `puts(normal_string)` part that does our job for us. The variable **normal_string** has inside the string `/bin/sh` so we just need to change the value of puts in the got table to point to system and this is how we will get shell.

![exploit](format_string_3-exploit.py)

flag: `picoCTF{G07_G07?_92325514}`