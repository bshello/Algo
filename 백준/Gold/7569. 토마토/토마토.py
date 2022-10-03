from collections import deque

def bfs(Q):
    while Q:
        h, y, x, k = Q.popleft()
        qk = k + 1
        for w in range(6):
            qh = h + dh[w]
            qy = y + dr[w]
            qx = x + dc[w]
            if 0 <= qh < H and 0 <= qy < M and 0 <= qx < N:
                if visited[qh][qy][qx] == 0 or visited[qh][qy][qx] > qk:
                    visited[qh][qy][qx] = qk
                    Q.append((qh, qy, qx, qk))

N, M, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
dr = (0, 0, 1, -1, 0, 0)
dc = (1, -1, 0, 0, 0, 0)
dh = (0, 0, 0, 0, 1, -1)
visited = [[[0] * N for _ in range(M)] for _ in range(H)]

Q = deque()
for i in range(H):
    for j in range(M):
        for k in range(N):
            if tomato[i][j][k] == -1:
                visited[i][j][k] = -1
            elif tomato[i][j][k] == 1:
                visited[i][j][k] = 1
                Q.append((i, j, k, 1))

bfs(Q)

ans = -0xffffff
stop = 0
for i in range(H):
    if stop == 1:
        break
    for j in range(M):
        if stop == 1:
            break
        for k in range(N):
            if visited[i][j][k] == 0:
                stop = 1
                ans = 0
                break
            if visited[i][j][k] > ans:
                ans = visited[i][j][k]

print(ans - 1)