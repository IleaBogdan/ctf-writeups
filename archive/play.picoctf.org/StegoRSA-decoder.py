from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
import base64

private_key_pem = '''-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCx0rX0ruL4gO6b
u3r1Zj37nYqEfrfZ3NpNOvzxmUNGzoKdE/fMluB7IPyDS2Af/B8xNbimvajmZDGu
UbD6VqjXOxY0aUpQO6rXPhQeh5+ZKbORQo83r+WdzWVnG39yLr0TgHaY+uSUBO5x
4sgRPpBbs6u2HHEjtk2R+/VjoZE4UgdZu6c1j6wAPFC43lzMTbtJ+MSiM8SaHIJA
3toXPkj3t0HGOVu3KWDKV9Vk4q/ieukM/f1clss5BBV7qG4m7Wuvm1arb9pAheCz
JqkFkihWkDfZyIJkzfOMy3+82zHAOf6iPsrsMo4uDfMp1n6L5E2hlYjpKHlKWfMN
DnYjGSr9AgMBAAECggEADK1lP/m04DsO58bcrACbRCQ14x7GnC9Y198v98hxqatg
1/J7vNf3zodqQTD/PCCFF8TI8og8cZpsiU01JQ/HDzsc6OUlwWUTl69LD2cjW2/D
58P7QmDVqaOiSlDFS/5lh+2lZuAiKiRU3IUqtsIDWCpNwFi0PzPIwXLZSn5TBFUE
RYcq2YX+Ibma8vKdO+WIq+boIsWW3fs3pJyi+/K2UcZ+Q2CXUYn24G53dTZrzKxG
70FmRPB5H2xuA4KwwqvbF4LH3E7+8AkGGk78/F78AhheomgSqUAt7y9zR2vmS/+/
21Ds/tRnt2WktspWpti3uYNWXj7tesKFSZmoxKPMYQKBgQDlOQ8eWiZ5K6Cbs3dk
wlwZMlUZtFRCNVOnwc5Ko1Zv+67C0pXq9SKYrM2bPA2IOPUaSKJmYja2kByzfdOa
4A428hb2bW95JxdECuJbBAhHQGfZCkh2gqRGW09EzLWfNH2qOwHAKYPRI/J+Dynf
kbbhYgHmx7WwlDEqFDN8S/2i3QKBgQDGmIiuId4ri4RXuMlS0/IfYHd9ajzW1lzo
QiYFC2hHMs7B1PoRpXNsogHX4YcsEVk6lNXNEO+onc5AJbVcLmMrvADsnQSZNEg1
jHgDCAv2CjvICU7B9y8hwZDqf1IzsYaPRfNmFYTqjgMRsEChRLN+dDNbeOuu2nVv
ljE9IqXWoQKBgFAGe6C9GHF1Kb0yCpzCviSNzegLbN8wfuQyZTLpk2PFGl4p5u0A
Z/OlYKKxdIf6Wpeyg//6id9ysJJ5e0a2sj+8hQfDbQd+/kBjDGN6JOm7MoYzcNjv
AysM9b+vODk8uiKUNyg/ViXNxvr7kELdPFuzO7a2QlhDZGasZs0eOo6BAoGBAIdE
2Dw7Z1ejpRYXEFHxeUaz70+mcCApTIkKnVjsRy/PxJK0HUyttCv3QWgo/mgevPcw
71vJQGRKcHSy+o/6LKRaXwrLfJlZyiFnN0thTLxehg+ff1yQoDLO5IVFCdmZ/rxR
+hK7b5hP+Hkw4yS1ZckpHt4cQ/QKatkBpTIuCmVhAoGAPuloXDtiveirkWoGqPyS
TJWn5JefEwhxDZ7Ta9qmxjoox0SAOcCUKNIZECY4l9hUtDiwIAcXuJTibTILwHlR
vI8YK+UsUxChFJqDaxfCbYUqt+yvWhOYy4iO8n9rDpa/DNP9/m+j0KoClJYwVkM1
k5Iy7bZWFOtvRW9ZwrxxGhM=
-----END PRIVATE KEY-----'''

key = RSA.import_key(private_key_pem)

with open("flag.enc", "rb") as file:  
    ciphertext = file.read()

cipher_rsa = PKCS1_v1_5.new(key)
plaintext = cipher_rsa.decrypt(ciphertext, None)

print("Decrypted text:")
print(plaintext.decode('utf-8', errors='ignore'))