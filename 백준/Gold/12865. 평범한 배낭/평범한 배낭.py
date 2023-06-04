import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Item = [(0, 0)]
W = [0] * (M + 1)
chart = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(N):
    w, v = map(int, input().split())
    Item.append((w, v))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        w = Item[i][0]
        v = Item[i][1]

        if j < w:
            chart[i][j] = chart[i - 1][j]
        else:
            chart[i][j] = max(chart[i - 1][j], v + chart[i - 1][j - w])

print(chart[-1][-1])