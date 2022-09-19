temp = []
s = 0
for _ in range(10):
    temp.append(int(input()))

for i in range(len(temp)):
    s += temp[i]
    if s >= 100:
        break

a = s
b = s - temp[i]
if abs(100 - a) <= abs(100 - b):
    ans = a
else:
    ans = b

print(ans)
