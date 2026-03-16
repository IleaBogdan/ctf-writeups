# dumb-discord

So we get a python code that is the source code of a discrord bot.
After reading the funtcions and understanding that it just xores some inputs with a mask: `mask = b'ctf{tryharderdontstring}'` I reversed all the coded inputs with the same function.
After that I invited the bot (https://discord.com/oauth2/authorize?client_id=783473293554352141&permissions=0&scope=bot%20applications.commands). The bot id was the one in the ifcondition at aroun the line ~48.

After that in my server I played with some commands and made myself the role it needed to give me the flag.
The right command to get a string you could put in the decoded function and decode to get the flag was:
> `@DCTFTargetWhyNot /s基ay /getFlag`

flag: `ctf{1b8fa7f33da67dfeb1d5f79850dcf13630b5563e98566bf7b76281d409d728c6}`