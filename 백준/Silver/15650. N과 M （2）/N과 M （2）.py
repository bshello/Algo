def dfs(N, M):
    global num
    tmp = num.copy()
    if len(num) == M:

        print(*num)
        return

    for i in range(1, N + 1):
        if i not in num:
            if len(num) >= 1:
                if i > num[-1]:
                    num.append(i)
                    dfs(N, M)
                    num.pop()
            else:
                num.append(i)
                dfs(N, M)
                num.pop()

N, M = map(int, input().split())
num = []
dfs(N, M)