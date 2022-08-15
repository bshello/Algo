dwarf = list()
m = 9
for _ in range(m):
    n = int(input())
    dwarf.append(n)
result = list()
for i in range(1<<m):
    temp = []
    for j in range(m):
        if i & (1<<j):
            temp.append(dwarf[j])
        if len(temp) == 7:
            if sum(temp) == 100:
                temp.sort()
                result.append(temp)
for k in range(7):
    print(result[0][k])