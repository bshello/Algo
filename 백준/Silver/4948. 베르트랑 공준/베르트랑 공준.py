res = []
while True:
    n = int(input())
    if n == 0:
        break

    m = 2 * n + 1
    arr = [True] * (m)

    for i in range(2, m):
        if arr[i] == True:
            for j in range(2*i, m, i):
                arr[j] = False

    cnt = 0
    for i in range(n+1, m):
        if arr[i] == True:
            cnt += 1

    ans = cnt
    if n == 1:
        ans = 1
    res.append(ans)

for i in res:
    print(i)