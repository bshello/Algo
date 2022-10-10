def bfs():
    global s
    while Q:
        r, c = Q.popleft()
        visited[r][c] = 1
        for j in range(4):
            qr = r + dr[j]
            qc = c + dc[j]
            if 0 <= qr < N and 0 <= qc < M:
                if arr[qr][qc] == 0 and not visited[qr][qc]:
                    visited[qr][qc] = 1
                    s += 1
                    Q.append((qr, qc))

from collections import deque
from itertools import combinations
N, M = map(int, input().split())
virus = deque()
mapsize = N * M
viruscnt = 0
wallcnt = 3
wall = []
arr = []
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 2:
            viruscnt += 1
            virus.append((i, j))
        elif tmp[j] == 1:
            wallcnt += 1
        else:
            wall.append((i, j))
    arr.append(tmp)

mapsize -= (viruscnt + wallcnt)
ans = 0
walltemp = combinations(wall, 3)
for i in walltemp:
    s = 0
    visited = [[0] * M for _ in range(N)]
    (r1, c1) = i[0]; (r2, c2) = i[1]; (r3, c3) = i[2]
    arr[r1][c1] = 1; arr[r2][c2] = 1; arr[r3][c3] = 1
    Q = virus.copy()
    bfs()
    arr[r1][c1] = 0; arr[r2][c2] = 0; arr[r3][c3] = 0
    ans = max(ans, mapsize - s)

print(ans)

