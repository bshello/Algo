iin = list()
out = list()
s = 0
temp = 0
for _ in range(4):
    n, m = map(int, input().split())
    iin.append(m)
    out.append(n)

for i in range(4):
    s += iin[i] - out[i]
    if temp < s:
        temp = s
        
print(temp)