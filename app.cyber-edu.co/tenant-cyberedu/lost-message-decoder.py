import sys, random, binascii, hashlib, re, math, os
from string import ascii_uppercase as asc
from itertools import product as d
ct="FNFWCiZJGWWAWZTKYLLKDVNiWCVYViBYHXDiXFBEMiKYEZQMMPKNRiQXZVBQ"

upper = {ascii:chr(ascii) for ascii in range(65,91)}
lower = {ascii:chr(ascii) for ascii in range(97,123)}
digit = {ascii:chr(ascii) for ascii in range(48,58)}

def dec2(st):
    dct1=""
    for c in st:
        if ord(c) in digit:
            dct1+=c
        else:
            o=ord(c)
            if o in upper and o-9 in upper:
                dct1+=chr(o-9)
            elif o in lower and o-9 in lower:
                dct1+=chr(o-9)
            else:
                dct1+=chr(o+17)
    return dct1

cipher=dec2(ct)
print(cipher)

def dec1(st):
    key="zxdfiuypka"
    key_lst = sorted(list(key)) 
    col = len(key) 
    print(col)
    row=len(st)//col
    matrix=[["A"for _ in range(col)]for _ in range(row)]
    k_indx=0
    idx=0
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for i in range(row):
            matrix[i][curr_idx]=st[idx]
            idx+=1
        k_indx+=1
    # print(matrix)
    dc=''.join(''.join(_)for _ in matrix)
    dc=dc.replace('z','')
    # print(dc)
    return dc

enc3enc4=dec1(cipher)
print(enc3enc4)

# this is not done
# the input could have parts in lowecase
# or it could have parts that are not in asc
# or could have the letter J in it.
# I don't like it
# maybe the other enc functions restrict stuff after all
def dec3(st):
    key="recomanded"
    s=['R','E','C','O','M','A','N','D','B','F','G','H','I','K','L','P','Q','S','T','U','V','W','X','Y','Z']
    m=[s[i:i+5] for i in range(0,len(s),5)]
    enc={row[i]+row[j]:row[(i+1)%5]+row[(j+1)%5] for row in m for i,j in d(range(5),repeat=2) if i!=j}
    enc.update({col[i]+col[j]:col[(i+1)%5]+col[(j+1)%5] for col in zip(*m) for i,j in d(range(5),repeat=2) if i!=j})
    enc.update({m[i1][j1]+m[i2][j2]:m[i1][j2]+m[i2][j1] for i1,j1,i2,j2 in d(range(5),repeat=4) if i1!=i2 and j1!=j2})
    
    rev_enc={}
    for e in enc:
        # print(e)
        rev_enc[enc[e]]=e
    # print(rev_enc)
    # print(enc)
    l=[]
    for i in range(0,len(st),2):
        l.append([rev_enc[st[i:i+2]][0],rev_enc[st[i:i+2]][1]])
    # print(l)
    return ''.join(''.join(_) for _ in l)

ct_enc4=dec3(enc3enc4)
print(ct_enc4)

def dec4(st):
    key=13
    r = [['\n' for i in range(len(st))] for j in range(key)]
    idx=0
    dir_down = False
    row, col = 0, 0
    for i in range(len(st)): 
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 
        r[row][col] = idx
        idx+=1
        col += 1
        if dir_down: 
            row += 1
        else: 
            row -= 1
    idx=0
    dc=["A" for _ in range(len(st))]
    for i in range(key):
        for j in range(len(st)):
            if '\n'!=r[i][j]:
                dc[r[i][j]]=st[idx]
                idx+=1
    return ''.join(dc)

dct=dec4(ct_enc4)
print(dct)

def postmessage(st):
    return st.replace("Q","_")
print(postmessage(dct))