from collections import deque

def bfs(r, c, s):
    global stop, check
    visited[r][c] = 1
    Q.append((r, c))
    cor.append((r, c))
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            qr = r + dr[i]
            qc = c + dc[i]
            if 0 <= qr < N and 0 <= qc < N:
                if L <= abs(arr[r][c] - arr[qr][qc]) <= R and not visited[qr][qc]:
                    check = True
                    visited[qr][qc] = 1
                    s += arr[qr][qc]
                    Q.append((qr, qc))
                    cor.append((qr, qc))
    x = len(cor)
    while cor:
        r, c = cor.popleft()
        visited[r][c] = s // x


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dc = (1, -1, 0, 0)
dr = (0, 0, 1, -1)
Q = deque()
cor = deque()
ans = 0
check = True
while check:
    check = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
               bfs(i, j, arr[i][j])

    arr = visited
    if check == True:
        ans += 1

print(ans)