N, K = map(int, input().split())
arr = [True] * (N+1)
cnt = 0
ans = 0
for i in range(2, N+1):
    if cnt == K:
        break
    for j in range(i, N+1, i):
        if arr[j] == True:
            arr[j] = False
            cnt += 1
        if cnt == K:
            ans = j
            break

print(ans)
