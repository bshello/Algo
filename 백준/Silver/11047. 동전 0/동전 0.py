n, k = map(int, input().split())
clist = list()
for i in range(n):
    coin = int(input())
    clist.append(coin)
temp = dict()
for j in range(n-1,-1,-1):
    s = k // clist[j]
    if s >= 1:
        k = k - (s*clist[j])
        temp.update({clist[j]:s})
    else:
        temp.update({clist[j]:s})
ans = 0
for key, value in temp.items():
    ans+=value
print(ans)