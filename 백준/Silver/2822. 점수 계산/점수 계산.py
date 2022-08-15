T = 8
lst = list()
for tc in range(T):
    n = int(input())
    lst.append(n)
ans = sorted(lst)
s = 0
idx = list()
for i in range(3,T):
    s += ans[i]
    for j in range(T):
        if ans[i] == lst[j]:
            idx.append(j+1)
idx.sort()
print(s)
print(*idx)