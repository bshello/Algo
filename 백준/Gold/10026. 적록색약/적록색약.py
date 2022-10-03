import sys
sys.setrecursionlimit(10000)

def dfs(y, x, z):
    for k in range(4):
        ty = y + dr[k]
        tx = x + dc[k]
        if 0 <= tx < N and 0 <= ty < N and not visited[ty][tx]:
            if RGB[ty][tx] == z:
                visited[ty][tx] = 1
                dfs(ty, tx, z)
    return

def rgbdfs(y, x, z):
    for k in range(4):
        ty = y + dr[k]
        tx = x + dc[k]
        if 0 <= tx < N and 0 <= ty < N and not rgbvisited[ty][tx]:
            if z in ['R', 'G']:
                if RGB[ty][tx] in ['R', 'G']:
                    rgbvisited[ty][tx] = 1
                    rgbdfs(ty, tx, z)
            else:
                if RGB[ty][tx] == z:
                    rgbvisited[ty][tx] = 1
                    rgbdfs(ty, tx, z)
    return





N = int(input())
RGB = [list(input()) for _ in range(N)]
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
visited = [[0] * N for _ in range(N)]
rgbvisited = [[0] * N for _ in range(N)]
cnt = 0
rgbcnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            dfs(i, j, RGB[i][j])
        if not rgbvisited[i][j]:
            rgbvisited[i][j] = 1
            rgbcnt += 1
            rgbdfs(i, j, RGB[i][j])


print(cnt, rgbcnt)