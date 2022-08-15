start, end = map(int, input().split())
num = list()
for i in range(1001):
    for j in range(i):
        num.append(i)
s = 0
for k in range(start-1, end):
    s += num[k]
print(s)