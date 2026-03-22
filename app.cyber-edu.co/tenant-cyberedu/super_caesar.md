# super_caesar

This ctf tells us there are 2 caeser cyphers that the ct was encoded with.
After playing around in dcode.fr with the ct I figured out that all the big letters are ecoded with (ord('U')-ord('S')==2) and the small ones are (ord('b')-ord('s')==9). This observation was made after I found out that the string `bcjac` becomes `start` and the string `UVQR` becomes `STOP`.

After decoding all the letters this way we get this text:
`WelLdONEyOUhAVESolVeDThiSTASKyOurFlAGisBGtSheIosNMPWRqTABZcdYhkIeCHtgCB`

At first I didn't read the text and pasted in and got wrong, but after reading it we can se that it says:
`WelL dONE yOU hAVE SolVeD ThiS TASK yOur FlAG is BGtSheIosNMPWRqTABZcdYhkIeCHtgCB`

So the answer the ctf wants is `BGtSheIosNMPWRqTABZcdYhkIeCHtgCB`.

decodeer script:
![[super_caeser_decoder.py]]

flag: `ECSC{BGtSheIosNMPWRqTABZcdYhkIeCHtgCB}`