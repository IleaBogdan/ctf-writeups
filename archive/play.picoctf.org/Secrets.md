# Secrets

After running a dirsearch on the url we get that it has a folder named **secret**.
So I made a dirsearch on it. 
I found a sub-folder named **assets**, however I was getting 403 on it and it had no sub-folders.

One thing I saw after inspecting the source code of `/secret/` is it had a css file in a subfolder named **hidden**.
No sub-folders in there tho.

But by viewing the source code of the `/hidden/` endpoint I found a sub-folder named **superhidden**. 
Upon entering it I found the flag.

Final path from root: `/secret/hidden/superhidden/`

flag: `picoCTF{succ3ss_@h3n1c@10n_39849bcf}`