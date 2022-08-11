n = int(input())
lst = list()
old = 0
oldman = list()
young = 20110000
youngman = list()

for i in range(n):
    a = list(input().split())
    lst.append(a)

for j in range(n):
    lst[j].append(0)

    if int(lst[j][1]) <10:
        lst[j][1] = '0'+lst[j][1]

    if int(lst[j][2]) <10:
        lst[j][2] = '0' + lst[j][2]

    lst[j][4] = (lst[j][3] + lst[j][2] + lst[j][1])

for k in range(n):
    if int(lst[k][4]) > old:
        old = int(lst[k][4])
        oldman.append(lst[k][0])

    if int(lst[k][4]) < young:
        young = int(lst[k][4])
        youngman.append(lst[k][0])

print(oldman[-1])
print(youngman[-1])
