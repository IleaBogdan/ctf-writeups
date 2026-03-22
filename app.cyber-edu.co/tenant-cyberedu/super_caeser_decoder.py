with open("flag","r")as file:
    flag=file.read()

print(flag)

ct=flag.split(" --- ")[1]
print(ct)

# bcjac -> start
# UVQR -> STOP

def stupid_caeser_decode(msg,ofs1,ofs2):
    nmsg=""
    for c in msg:
        if not c.isalpha():
            nmsg+=c
            continue
        # print(c)
        if c.islower():
            nmsg+=chr(ord('a')+(26+ord(c)-ord('a')-ofs1)%26)
        else:
            nmsg+=chr(ord('A')+(26+ord(c)-ord('A')-ofs2)%26)
    return nmsg

ofs1=(26+ord('b')-ord('s'))%26
ofs2=(26+ord('U')-ord('S'))%26

print(stupid_caeser_decode(ct,ofs1,ofs2))