# easy-hide

After downloading the image and looking at exiftool I decided to do a binwalk on the file:
```sh
binwalk strange-final.jpg -e 2>/dev/null
```

And it extracted some folder named `_strange-final.jpg.extracted`.
Inside was a zip file and a png image.
I tried opening it and it failed.
So I looked at the headers and saw this:
```
00000000: 6272 6f6b 656e 7a69 6e73 6964 6572 6570  brokenzinsiderep
```
This is not a valid png header and not a valid header for any file format.

So I decided to change the bytes of the file to be a PNG header.
It didn't work. So I tried another format. (JFIF)
```
00000000: ffd8 ffe0 0010 4a46 4946 0001 6572 6570  ......JFIF..erep
```

This time it worked. And when I opened the image I saw the flag.

flag: `UNR{sunIZZsunshine}`