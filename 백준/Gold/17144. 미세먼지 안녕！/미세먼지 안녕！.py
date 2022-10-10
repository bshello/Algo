def shift1():
    res = dustmap[W[0]][1]
    for i in range(2, C):
        dustmap[W[0]][i], res = res, dustmap[W[0]][i]
    dustmap[W[0]][1] = 0
    for i in range(W[0] -1, -1, -1):
        dustmap[i][C - 1], res = res, dustmap[i][C - 1]
    for i in range(C - 2, -1, -1):
        dustmap[0][i], res = res, dustmap[0][i]
    for i in range(1, W[0]):
        dustmap[i][0], res = res, dustmap[i][0]

def shift2():
    res = dustmap[W[1]][1]
    for i in range(2, C):
        dustmap[W[1]][i], res = res, dustmap[W[1]][i]
    dustmap[W[1]][1] = 0
    for i in range(W[1] + 1, R):
        dustmap[i][C - 1], res = res, dustmap[i][C - 1]
    for i in range(C - 2, -1, -1):
        dustmap[R - 1][i], res = res, dustmap[R - 1][i]
    for i in range(R - 2, W[1], -1):
        dustmap[i][0], res = res, dustmap[i][0]

from collections import deque
Q = deque()
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
R, C, T = map(int, input().split())
W = []
for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        if tmp[j] > 0:
            Q.append((i, j, tmp[j]))
        elif tmp[j] == -1:
            W.append(i)
k = 0
while k < T:
    dustmap = [[0] * C for _ in range(R)]
    dustmap[W[0]][0] = -1
    dustmap[W[1]][0] = -1

    while Q:
        r, c, dust = Q.popleft()
        qdust = dust // 5
        for i in range(4):
            qr = r + dr[i]
            qc = c + dc[i]
            if qdust > 0:
                if 0 <= qr < R and 0 <= qc < C and dustmap[qr][qc] != -1:
                    dustmap[qr][qc] += qdust
                    dust -= qdust
            else:
                break
        dustmap[r][c] += dust
    shift1()
    shift2()

    for i in range(R):
        for j in range(C):
            if dustmap[i][j] > 0:
                Q.append((i, j, dustmap[i][j]))

    k += 1

ans = 0
for i in range(R):
    for j in range(C):
        ans += dustmap[i][j]
print(ans + 2)
