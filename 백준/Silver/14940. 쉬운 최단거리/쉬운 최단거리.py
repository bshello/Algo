import sys
from collections import deque

def checkRange(row, column):

    if 0 <= row < n and 0 <= column < m:
        return True

    return False


input = sys.stdin.readline
n, m = map(int, input().split())
delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
obj = set()
ans = [[0] * m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            goalx = j
            goaly = i
        elif tmp[j] == 0:
            obj.add((i, j))

visited = [[0] * m for _ in range(n)]
visited[goaly][goalx] = 1
for o, b in obj:
    visited[o][b] = 1
Q = deque()
Q.append((goaly, goalx, 0))

while Q:
    y, x, depth = Q.popleft()

    for r, c in delta:
        dy = r + y
        dx = c + x

        if checkRange(dy, dx):
            if not visited[dy][dx]:
                visited[dy][dx] = 1
                ans[dy][dx] = depth + 1
                Q.append((dy, dx, depth + 1))

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            ans[i][j] = -1

for i in ans:
    print(*i)