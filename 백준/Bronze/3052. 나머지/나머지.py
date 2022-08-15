n = 10
num = list()
for _ in range(n):
    m = int(input())
    num.append(m)
rem = list()
for i in num:
    rem.append(i%42)
remdict = dict()
for j in rem:
    if j in remdict:
        remdict[j] += 1
    else:
        remdict.update({j:1})
cnt = 0
for k in remdict:
    cnt += 1
    
print(cnt)