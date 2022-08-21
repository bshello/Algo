t = int(input())
m = list()
for _ in range(t):
    n = list(map(int, input().split()))
    m.append(n)
m.sort()
midx1 = list()
midx2 = list()
idx1 = t
idx2 = -1
cnt = 0
while True:
    ma1 = 0
    ma2 = 0
    if idx1 != 0:
        for i in range(idx1):
            if ma1 < m[i][1]:
                ma1, idx1 = m[i][1], i
        midx1.append(idx1)
    if idx2 != t-1:
        for j in range(idx2+1, t):
            if ma2 < m[j][1]:
                ma2, idx2 = m[j][1], j
        midx2.append(idx2)

    if idx1 == 0 and idx2 == t-1:
        break
    cnt+=1
    if cnt > t:
        break

ans = m[midx1[0]][1]
if len(midx1) > 1:
    for i in range(len(midx1)-1):
        ans += (m[midx1[i]][0] - m[midx1[i+1]][0]) * m[midx1[i+1]][1]

if len(midx2) > 1:
    for j in range(len(midx2)-1):
        ans += abs(m[midx2[j]][0] - m[midx2[j+1]][0]) * m[midx2[j+1]][1]

print(ans)