import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd(graph, N):

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j: graph[i][j] = 1
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph

N, M = map(int, input().split())
friend = [[N] * N for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    friend[A - 1][B - 1] = 1
    friend[B - 1][A - 1] = 1

floyd(friend, N)
min_bakon = sys.maxsize
ans = N
for i in range(N):
    tmp = sum(friend[i])
    if tmp < min_bakon:
        min_bakon = tmp
        ans = i
print(ans + 1)