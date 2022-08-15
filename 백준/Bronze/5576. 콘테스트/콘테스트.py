nlst = list()
mlst = list()
for _ in range(10):
    n = int(input())
    nlst.append(n)
    nlst.sort()
    sn = 0
for i in range(7,10):
    sn += nlst[i]
for _ in range(10):
    m = int(input())
    mlst.append(m)
    mlst.sort()
    sm = 0
for j in range(7, 10):
    sm += mlst[j]

print(sn, sm)
