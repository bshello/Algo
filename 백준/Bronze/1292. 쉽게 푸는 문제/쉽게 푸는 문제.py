s, e = map(int, input().split())
temp = []
for i in range(1, (e//2)+2):
    for j in range(i):
        temp.append(i)
se = 0
for i in range(s-1, e):
    se += temp[i]

print(se)