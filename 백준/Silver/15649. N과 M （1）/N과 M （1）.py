def dfs(N, M):
    global num

    if len(num) == M:
        print(*num)
        return

    for i in range(1, N + 1):
        if i not in num:
            num.append(i)
            dfs(N, M)
            num.pop()

N, M = map(int, input().split())
num = []
dfs(N, M)



