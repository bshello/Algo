def dfs(y, x):
    global cnt
    for k in range(4):
        ty = y + dr[k]
        tx = x + dc[k]
        if 0<= tx < N and 0<= ty < N and not visited[ty][tx]:
            if town[ty][tx] == 1:
                visited[ty][tx] = 1
                cnt += 1
                dfs(ty, tx)

N = int(input())
town = [list(map(int, input())) for _ in range(N)]
num = 1
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
visited = [[0] * N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            cnt = 1
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in ans:
    print(i)