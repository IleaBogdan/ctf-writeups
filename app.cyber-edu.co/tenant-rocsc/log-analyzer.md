# log-analyzer

After unziping the file, we run cat on the log.txt file and then pipe the output to a grep "CTF{" and this will give us our flag.

```shell
unzip log-analyzer.zip ; cat log-analyzer/log.txt | grep "CTF{"
```

flag: `CTF{b31cf6c1f7b056ce06e207aa6cdcfa7577a98b90042728923cc577f8b62448df}`