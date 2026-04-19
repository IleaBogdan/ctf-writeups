# RedLine

##### Q1:

I listed all the procceses and this one caught mt eyes: `oneetx.exe`
```
volatility3 -f MemoryDump.mem windows.pslist.PsList
```  

flag q1: `oneetx.exe`

##### Q2:

After running:
```sh
volatility3 -f MemoryDump.mem windows.pstree.PsTree | grep "oneetx.exe"
```
I got that the `oneetx.exe` apears 2 times in the pstree. So I looked to see which of the 2 pids apear as parrent pids and I go that this procces has the ppid from one of the 2:
`* 7732	5896	rundll32.exe	0xad818d1912c0	1	-	1	True	2023-05-21 22:31:53.000000 UTC	N/A	\Device\HarddiskVolume3\Windows\SysWOW64\rundll32.exe` 

flag q2: `rundll32.exe`

##### Q3:

After running:
```sh
volatility3 -f MemoryDump.mem windows.vadinfo --pid 5896
```

After that I looked at the Protection tab and I tried some of them.

flag q3: `PAGE_EXECUTE_READWRITE`

##### Q4:

After looking in the pslist I saw that there is a tun2socks.exe. So I looked to see what process spawned it and I got this: `Outline.exe`

flag q4: `Outline.exe`

##### Q5:

After running:
```sh
volatility3 -f MemoryDump.mem windows.netscan.NetScan
```
I saw this: `0xad818de4aa20	TCPv4	10.0.85.2	55462	77.91.124.20	80	CLOSED	5896	oneetx.exe	2023-05-21 23:01:22.000000 UTC`

flag q5: `77.91.124.20`

##### Q6:

Since we know tha attackers ip we can strings and grep via the ip.
Or `strings MemoryDump.mem| grep http | grep php`, but this one still brings up a lot of memory.

flag q6: `http://77.91.124.20/store/games/index.php`

##### Q7:

After runnning strings on the binary we can grep for oneetx.exe and we get the flag.

flag q5: `C:\Users\Tammam\AppData\Local\Temp\c3912af058\oneetx.exe`