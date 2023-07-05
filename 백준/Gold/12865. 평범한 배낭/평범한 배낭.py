import sys

input = sys.stdin.readline

N, K = map(int, input().split())
bag = [[0] * (K + 1) for _ in range(N + 1)]
stuff = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    stuff.append((W, V))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(bag[i - 1][j - weight] + value, bag[i - 1][j])
print(bag[N][K])
