n = 9
d = [input() for _ in range(n)]
dwarf = list(map(int, d))
res = list()
for i in range(1 << n):
    temp = list()
    for j in range(n):
        if i & (1 << j):
            temp.append(dwarf[j])
    if len(temp) == 7:
        if sum(temp) == 100:
            res.append(temp)

res[0].sort()
for i in res[0]:
    print(i)