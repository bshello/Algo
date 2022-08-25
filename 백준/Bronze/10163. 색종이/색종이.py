n = int(input())
m = 1001
sqr = [list(map(int, input().split())) for _ in range(n)]
arr = [[0]*m for _ in range(m)]
ans = list()
mar = 0
mac = 0
for i in range(n):
    c = sqr[i][0]
    w = sqr[i][2]
    r = m - sqr[i][1] - 1
    h = sqr[i][3]

    for y in range(r-h+1, r+1):
        for x in range(c, c+w):
            arr[y][x] = i+1

    if mar < r+1:
        mar = r+1
    if mac < c+w:
        mac = c+w

for i in range(n):
    s = 0
    for j in range(mar):
        for k in range(mac):
            if arr[j][k] == i+1:
                s += 1
    ans.append(s)

for i in ans:
    print(i)
