n = int(input())
m = n
i = n//2
res = list()
ma = 0
idx = 0
while i<=n:
    ans = [n, i]
    while True:
        n = ans[-2] - ans[-1]
        if n<0:
            break
        ans.append(n)
    if ma < len(ans):
        ma = len(ans)
    i += 1
    res.append(ans)
    n = m

for j in range(len(res)):
    if len(res[j]) == ma:
        idx = j
print(ma)
print(*res[idx])
