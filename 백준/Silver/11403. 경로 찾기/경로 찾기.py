import sys
input = sys.stdin.readline

def floyd(graph, N):

    dist = [[0xffffff] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                dist[i][j] = graph[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = floyd(graph, N)
for i in range(N):
    for j in range(N):
        if ans[i][j] >= 0xffffff:
            ans[i][j] = 0
        else:
            ans[i][j] = 1

for i in range(N):
    print(*ans[i])