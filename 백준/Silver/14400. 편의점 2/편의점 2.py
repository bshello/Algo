n = int(input())

xl = []
yl = []
for _ in range(n):
    x, y = map(int, input().split())
    xl.append(x)
    yl.append(y)

xl.sort()
yl.sort()


tempx1 = 0
tempx2 = 0
tempy1 = 0
tempy2 = 0

for i in xl:
    tempx1 += abs(i - xl[n // 2])
    tempx2 += abs(i - xl[n//2 - 1])
for j in yl:
    tempy1 += abs(j - yl[n // 2])
    tempy2 += abs(j - yl[n // 2 - 1])

if tempx1 >= tempx2:
    ansx = tempx2
else:
    ansx = tempx1

if tempy1 >= tempy2:
    ansy = tempy2
else:
    ansy = tempy1

ans = ansx + ansy

print(ans)