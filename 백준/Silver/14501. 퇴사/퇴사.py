def dfs(day, pay):
    global ans

    ans = max(ans, pay)

    for j in range(day, N):
        if j + task[j][0] <= N and not visited[j]:
            visited[j] = 1
            dfs(j + task[j][0], pay + task[j][1])
            visited[j] = 0
        if j == N - 1:
            return

N = int(input())
task = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
ans = -0xffffff
dfs(0, 0)
print(ans)
