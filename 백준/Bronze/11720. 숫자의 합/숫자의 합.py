n = int(input())
m = list(input())
l = list()
for j in range(n):
        l.append(m[j])
s = 0
ans = list(map(int, l))
for k in range(n):
    s += ans[k]

print(s)