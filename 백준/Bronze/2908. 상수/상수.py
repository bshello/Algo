n, m = map(str, input().split())
num = list(n)
mum = list(m)
num.reverse()
mum.reverse()
nn = ''
mm = ''
for i in range(3):
    nn += num[i]
    mm += mum[i]

if int(nn) > int(mm):
    print(nn)
else:
    print(mm)