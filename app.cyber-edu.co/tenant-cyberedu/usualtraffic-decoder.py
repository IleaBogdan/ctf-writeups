from scapy.all import *
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

scapy_cap = rdpcap('traffic.pcapng')

def process_data(i):
    pkt=scapy_cap[i]
    if not (pkt.haslayer(TCP) and (pkt[TCP].sport == 179 or pkt[TCP].dport == 179)):return False
    if len(raw(pkt))!=123:return False
    return True

router1=""
router2=""
for i in range(len(scapy_cap)):
    if process_data(i):
        pkt=scapy_cap[i]
        # print(pkt.src)
        if pkt.src=="52:54:00:aa:2a:9e":
            router1+=raw(pkt).split(b'\x00d ')[-1].decode()
        else:
            router2+=raw(pkt).split(b'\x00d ')[-1].decode()


def decrypt_aes(ct, key, iv):
    key=bytes.fromhex(key)
    iv=bytes.fromhex(iv)
    ct=base64.b64decode(ct)
    cipher=AES.new(key,AES.MODE_CBC,iv)
    return unpad(cipher.decrypt(ct),AES.block_size).decode()

# print("-------")
# print(router1)
# print("-------")
# print(router2)

key=router1.split("\n")[1].split(":")[-1].strip()
secret1=router1.split("\n")[2].split(":")[-1].strip()
vector=router2.split("\n")[1].split(":")[-1].strip()
secret2=router2.split("\n")[2].split(":")[-1].strip()

print(key)
print(vector)
print(secret1)
print(secret2)
print()

print(decrypt_aes(secret1,key,vector)+decrypt_aes(secret2,key,vector))