N = int(input())
s = 0
for i in range(N+1):
    for j in range(i+1):
        s+= (i+j)
print(s)