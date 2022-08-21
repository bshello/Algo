n, m = map(int, input().split())
t = int(input())
temp = list()
xl = list()
xll = list()
yl = list()
yll = list()
for _ in range(t):
    a = list(map(int, input().split()))
    temp.append(a)

for i in range(t):
    if temp[i][0] == 0:
        xl.append(temp[i][1])
    else:
        yl.append(temp[i][1])
xl.sort()
yl.sort()
if len(xl) > 0:
    xll = [xl[0]]
if len(yl) > 0:
    yll = [yl[0]]

if len(xl) > 1:
    for j in range(1, len(xl)):
        xll.append(xl[j] - xl[j-1])
if len(yl) > 1:
    for k in range(1, len(yl)):
        yll.append(yl[k] - yl[k-1])

if len(xl) > 0:
    xll.append(m-xl[-1])
else:
    xll.append(m)

if len(yl) > 0:
    yll.append(n-yl[-1])
else:
    yll.append(n)

xll.sort()
yll.sort()

ans = xll[-1] * yll[-1]
print(ans)

