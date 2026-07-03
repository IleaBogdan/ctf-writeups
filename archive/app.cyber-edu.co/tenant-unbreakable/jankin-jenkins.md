# jankin-jenkins

Opening http://34.179.142.63:30146/loginError in Burp and saw: `X-Jenkins: 2.441`
Looking up CVEs for the 2.44 version of jenkins gave me CVE-2024-23897.

exploit poc: https://github.com/godylockz/CVE-2024-23897/blob/main/jenkins_fileread.py

Running the exploit poc allowed me to read each file on the server. 
Opening `/home/flag.txt` gave me the flag.

Flag 1: `2.441`
Flag 2: `CVE-2024-23897`
Flag 3: `CTF{a36f507ff69287bf3f49261f065167bb077d061b3d0d0d11d70b53b3ed3537d1}`