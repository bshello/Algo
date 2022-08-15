iin = list()
out = list()
s = 0
temp = 0
for _ in range(10):
    n, m = map(int, input().split())
    iin.append(m)
    out.append(n)

for i in range(10):
    s += iin[i] - out[i]
    if temp < s:
        temp = s

print(temp)