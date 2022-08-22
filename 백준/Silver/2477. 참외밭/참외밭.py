m = int(input())
sq = list()
for _ in range(6):
    x = list(map(int, input().split()))
    sq.append(x)

n = 0
nidx = 0
w = 0
widx = 0
for i in range(6):
    if sq[i][0] == 1 or sq[i][0] == 2:
        if n < sq[i][1]:
            n, nidx = sq[i][1], i
    else:
        if w < sq[i][1]:
            w, widx = sq[i][1], i

if nidx > widx:
    if nidx == 5 and widx != 4:
        a = widx + 2
        if a > 5:
            a -= 6
        b = widx + 3
        if b > 5:
            b -= 6
        ans = m * (n * w - sq[a][1] * sq[b][1])
    else:
        a = nidx + 2
        if a > 5:
            a -= 6
        b = nidx + 3
        if b > 5:
            b -= 6
        ans = m * (n * w - sq[a][1] * sq[b][1])
else:
    if widx == 5 and nidx != 4:
        a = nidx + 2
        if a > 5:
            a -= 6
        b = nidx + 3
        if b > 5:
            b -= 6
        ans = m * (n * w - sq[a][1] * sq[b][1])
    else:
        a = widx + 2
        if a > 5:
            a -= 6
        b = widx + 3
        if b > 5:
            b -= 6
        ans = m * (n * w - sq[a][1] * sq[b][1])

print(ans)