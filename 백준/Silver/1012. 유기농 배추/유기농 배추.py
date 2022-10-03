from collections import deque

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
for tc in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    k = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                k += 1
                visited[i][j] = 1
                Q = deque()
                Q.append((i, j))
                while Q:
                    y, x = Q.popleft()
                    for w in range(4):
                        qy = y + dy[w]
                        qx = x + dx[w]
                        if 0 <= qx < M and 0 <= qy < N:
                            if arr[qy][qx] == 1 and not visited[qy][qx]:
                                visited[qy][qx] = 1
                                Q.append((qy, qx))
    print(k)