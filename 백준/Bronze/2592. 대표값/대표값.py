num = list()
for _ in range(10):
    n = int(input())
    num.append(n)
s = 0
ndict = dict()
for i in num:
    s += i
    if i in ndict:
        ndict[i] += 1
    else:
        ndict.update({i:1})
temp = 0
for j in ndict.values():
    if temp < j:
        temp = j
avg = s/10
print(int(avg))
for key, value in ndict.items():
    if value == temp:
        print(key)

