N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, 0
cnt = 0
while e < N:
    res = sum(arr[s:e+1])

    if res == M:
        cnt += 1
        s += 1
        e += 1
    elif res > M:
        s += 1
    elif res < M:
        e += 1
print(cnt)

