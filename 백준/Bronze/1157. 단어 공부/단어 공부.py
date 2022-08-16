a = input()
n = a.upper()
m = dict()
for i in n:
    if i in m:
        m[i] += 1
    else:
        m.update({i:1})
temp = 0
for key, value in m.items():
    if temp < value:
        temp = value
ans = list()
for key, value in m.items():
    if temp == value:
        ans.append(key)

if len(ans)>1:
    print('?')
else:
    print(*ans)