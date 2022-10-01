from collections import deque

dr = (-1, -2, -2, -1, 1, 2, 2, 1)
dc = (-2, -1, 1, 2, 2, 1, -1, -2)
for tc in range(int(input())):
    N = int(input())
    knight = list(map(int, input().split()))
    tg = list(map(int, input().split()))
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    Q.append((knight[0], knight[1]))
    visited[knight[1]][knight[0]] = 1

    while Q:
        x, y = Q.popleft()
        if x == tg[0] and y == tg[1]:
            ans = visited[y][x] - 1
            break
        for i in range(8):
            qx = x + dc[i]
            qy = y + dr[i]
            if 0 <= qx < N and 0 <= qy < N and not visited[qy][qx]:
                visited[qy][qx] = visited[y][x] + 1
                Q.append((qx, qy))

    print(ans)