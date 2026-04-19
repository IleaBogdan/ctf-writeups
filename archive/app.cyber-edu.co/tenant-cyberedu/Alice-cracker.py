hashes=[]
with open("inputs.txt","r")as file:
    hashes=file.readlines()

print(len(hashes[0]))
ans=""
for i in range(32):
    d={}
    for j in range(len(hashes)):
        if hashes[j][i] not in d:
            d[hashes[j][i]]=0
        d[hashes[j][i]]+=1
    for h in d:
        if d[h]==1:
            ans+=h
print(len(ans))
print(ans)

for i in range(32,len(hashes[0])-1):
    d=set({})
    for j in range(len(hashes)):
        d.add(hashes[j][i])
    for h in "0123456789abcdef":
        if h not in d:
            ans+=h

print(ans)