# zodiac

If we open the file in wireshark we can see a lot of DNS querys and http querys on different sites (youtube.com, goolge.com, stackoverflow.com, reddit.com, etc.).
The ping commands have no response.

Looking at the addresses the ping comes from we can see that they differ and belong to digi, British Telecommunications Plc, etc.

We can follow the UDP stream and we will see a big string with this starting text.
`timestamp,x,y,left_button_holding,right_button_holding`
So the UDP packages is the trace of the mouse movement.

If we extract the data and then plot it with python we can get the png with the flag.
![plotter](zodiac-plotter.py)

![mouse.png](zodiac-mouse.png)

flag: `ctf{secretplacewukong'sden}`