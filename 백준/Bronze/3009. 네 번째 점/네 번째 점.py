xl = list()
xll = list()
xlll = list()
yl = list()
yll = list()
ylll = list()
for i in range(3):
    x, y = map(int, input().split())
    xl.append(x)
    yl.append(y)

for j in range(1,len(xl)):
    xll.append(xl[0])
    if xl[j] in xll:
        xll.append(xl[j])
    else:
        xlll.append(xl[j])

for k in range(1,len(yl)):
    yll.append(yl[0])
    if yl[k] in yll:
        yll.append(yl[k])
    else:
        ylll.append(yl[k])

if len(xll) > len(xlll):
    xx = xlll[0]
else:
    xx = xll[0]

if len(yll) > len(ylll):
    yy = ylll[0]
else:
    yy = yll[0]

print(xx, yy)