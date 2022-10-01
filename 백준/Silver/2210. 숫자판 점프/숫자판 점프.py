def dfs(x, y):
    if len(temp) == 6:
        tmp = temp.copy()
        if tmp not in res:
            res.append(tmp)
        return

    for i in range(4):
        tx = x + dc[i]
        ty = y + dr[i]
        if 0 <= tx < 5 and 0 <= ty <5:
            temp.append(arr[ty][tx])
            dfs(tx, ty)
            temp.pop()



arr = [list(map(int, input().split())) for _ in range(5)]
res = []
dc = (0, 0, 1, -1)
dr = (1, -1, 0, 0)
for k in range(5):
    for l in range(5):
        temp = [arr[k][l]]
        dfs(l, k)

print(len(res))