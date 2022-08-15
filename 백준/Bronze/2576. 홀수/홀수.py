num = list()
odd = list()
s = 0
temp = 1000000
for _ in range(7):
    n = int(input())
    num.append(n)

for i in num:
    if i%2 == 1:
        s += i
        odd.append(i)

for j in odd:
    if temp > j:
        temp = j

if len(odd) == 0:
    print(-1)
else:
    print(s)
    print(temp)