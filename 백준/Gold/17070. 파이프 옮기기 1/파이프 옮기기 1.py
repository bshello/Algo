def check(qr, qc, d):
    if arr[qr][qc] == 0:
        if d == 2:
            if arr[qr - 1][qc] == 0 and arr[qr][qc - 1] == 0:
                return True
            else:
                return False
        return True
    return False

def dfs(r, c, d):
    global cnt

    if r == c == N - 1:
        cnt += 1
        return

    for i in range(3):
        if dr[d][i] == -1:
            continue
        qr = r + dr[d][i]
        qc = c + dc[d][i]
        if 0 <= qr < N and 0 <= qc < N:
            if check(qr, qc, i):
                dfs(qr, qc, i)

dc = ((1, -1, 1), (-1, 0, 1), (1, 0, 1))
dr = ((0, -1, 1), (-1, 1, 1), (0, 1, 1))
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
if arr[N - 1][N - 1] == 1:
    print(0)
else:
    dfs(0, 1, 0)
    print(cnt)