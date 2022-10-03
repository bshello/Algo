from collections import deque

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
def bfs():
    while Q:
        y, x, k = Q.popleft()
        qk = k + 1
        for i in range(4):
            qy = y + dr[i]
            qx = x + dc[i]
            if 0 <= qx < N and 0 <= qy < M:
                if arr[qy][qx] == 0:
                    if visited[qy][qx] == 0 or visited[qy][qx] > qk:
                        visited[qy][qx] = qk
                        Q.append((qy, qx, qk))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = -0xffffff
Q = deque()
for i in range(M):
    for j in range(N):
        if arr[i][j] == -1:
            visited[i][j] = -1
        elif arr[i][j] == 1:
            visited[i][j] = 1
            Q.append((i, j, 1))
bfs()
stop = 0
for i in range(M):
    if stop == 1:
        ans = 0
        break
    for j in range(N):
        if visited[i][j] == 0:
            stop = 1
            break
        ans = max(ans, visited[i][j])

print(ans - 1)
