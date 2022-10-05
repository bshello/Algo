N, S = map(int, input().split())
l = list(map(int, input().split()))

s = l[0]
ans = 0xffffff
i = -1
j = 0
while True:
    if s < S:
        if j == N - 1:
            break
        j += 1
        s += l[j]
    else:
        ans = min(ans, j - i)
        i += 1
        s -= l[i]

if ans == 0xffffff:
    ans = 0
print(ans)
