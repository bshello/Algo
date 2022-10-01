from collections import deque
N, M = map(int, input().split())
visited = [0] * (200002)
Q = deque()
Q.append(N)
visited[N] = 1
while Q:
    q = Q.popleft()

    if q == M:
        ans = visited[q] - 1
        break

    if q + 1 <= 100000:
        if not visited[q + 1]:
            visited[q + 1] = visited[q] + 1
            Q.append(q + 1)

    if q - 1 >= 0:
        if not visited[q - 1]:
            visited[q - 1] = visited[q] + 1
            Q.append(q - 1)

    if q * 2 <= 100000:
        if not visited[q * 2]:
            visited[q * 2] = visited[q] + 1
            Q.append(q * 2)

print(ans)
