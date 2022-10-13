def check(i, j, n):
    if i + n <= 10 and j + n <= 10:
        r = i + n
        c = j + n
        for k in range(i, r):
            for l in range(j, c):
                if arr[k][l] != 1:
                    return False
        return True
    return False


def dfs(i, j, cnt):
    global ans
    if i > 9:
        ans = min(ans, cnt)
        return

    if cnt > ans:
        return

    if arr[i][j] == 1:
        for n in range(5, 0, -1):
            if paper[n] == 5:
                continue
            if check(i, j, n):
                for k in range(i, i+n):
                    for l in range(j, j+n):
                        arr[k][l] = 0
                paper[n] += 1
                if j == 9:
                    dfs(i + 1, 0, cnt + 1)
                else:
                    dfs(i, j + 1, cnt + 1)
                for k in range(i, i+n):
                    for l in range(j, j+n):
                        arr[k][l] = 1
                paper[n] -= 1
    else:
        if j == 9:
            dfs(i + 1, 0, cnt)
        else:
            dfs(i, j + 1, cnt)





arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0] * 6
visited = [[0] * 10 for _ in range(10)]
ans = 0xffffff
dfs(0, 0, 0)
if ans == 0xffffff:
    ans = -1
print(ans)

