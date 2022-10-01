def dfs(N, M):
    global num
    tmp = num.copy()
    if len(num) == M:

        print(*num)
        return

    for i in range(1, N + 1):
        num.append(i)
        dfs(N, M)
        num.pop()


N, M = map(int, input().split())
num = []
dfs(N, M)