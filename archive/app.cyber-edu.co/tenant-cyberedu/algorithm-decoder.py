def polinom(n, m):
    i = 0
    z = []
    s = 0
    while n > 0:
        if n % 2 != 0:
            z.append(2 - (n % 4))
        else:
            z.append(0)
        n = (n - z[i])//2
        i = i + 1
    z = z[::-1]
    l = len(z)
    for i in range(0, l):
        s += z[i] * m ** (l - 1 - i)
    return s

poslist=[]
rpos={}
for i in range(0,100):
    v=str(polinom(i,3))
    rpos[v]=str(i) if i>9 else "0"+str(i)
    poslist.append(v)

with open("flag_enc.txt","r")as file:
    ct=file.readlines()[0][:-1]
print(ct)

def valid_int(i):
    if i==0:return True
    return i.isdigit() and i[0]!='0'

sol=[]
def g(idx,val=""):
    if idx==len(ct):
        sol.append(int(val)//10+1)
        return
    for pos in poslist:
        if idx+len(pos)>len(ct):continue
        pref=ct[idx:idx+len(pos)]
        if not valid_int(pref):continue
        if pref!=pos:continue
        g(idx+len(pos),val+rpos[pos])
g(0,"")

print(sol)
for s in sol:
    h=hex(s)[2:]
    try:
        f=bytes.fromhex(h).decode()
        print("FLAG:")
        print(h)
        print(f)
        break
    except Exception as e:
        pass