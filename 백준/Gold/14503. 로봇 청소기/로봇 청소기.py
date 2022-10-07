def dfs(r, c, d):
    global cnt, stop
    for i in range(0, 10, 3):
        if stop == 1:
            return
        qd = (i + d) % 4
        qr = r + dr[qd]
        qc = c + dc[qd]
        if arr[qr][qc] == 0:
            arr[qr][qc] = cnt
            cnt += 1
            dfs(qr, qc, (qd + 3)%4)

    if d == 0:
        cr = r + dr[3]
        cc = c + dc[3]
        if arr[cr][cc] == 1:
            stop = 1
            return
        else:
            dfs(cr, cc, d)
    elif d == 1:
        cr = r + dr[0]
        cc = c + dc[0]
        if arr[cr][cc] == 1:
            stop = 1
            return
        else:
            dfs(cr, cc, d)

    elif d == 2:
        cr = r + dr[1]
        cc = c + dc[1]
        if arr[cr][cc] == 1:
            stop = 1
            return
        else:
            dfs(cr, cc, d)
    else:
        cr = r + dr[2]
        cc = c + dc[2]
        if arr[cr][cc] == 1:
            stop = 1
            return
        else:
            dfs(cr, cc, d)



N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# 서, 북, 동, 남
dr = (0, -1, 0, 1)
dc = (-1, 0, 1, 0)
cnt = 3
visited[r][c] = 1
arr[r][c] = 2
stop = 0
dfs(r, c, d)

print(cnt - 2)







