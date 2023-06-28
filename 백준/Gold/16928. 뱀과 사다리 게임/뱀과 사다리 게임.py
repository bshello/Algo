import sys
from collections import deque
N, M = map(int, input().split())
ladder = dict()
snake = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

Q = deque()
Q.append((1, 0))
ans = 0
visited = [0] * 200
visited[1] = 1
while Q:
    index, depth = Q.popleft()

    if index >= 100:
        ans = depth
        break

    for i in range(1, 7):
        tmp = index + i

        if tmp in ladder:
            tmp = ladder[tmp]
        elif tmp in snake:
            tmp = snake[tmp]

        if not visited[tmp]:
            visited[tmp] = 1
            Q.append((tmp, depth+1))

print(ans)