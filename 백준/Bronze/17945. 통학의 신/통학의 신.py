a, b = map(int, input().split())
ans = []
for i in range(-1000, 2000):
    if i**2 + 2*a*i + b == 0:
        ans.append(i)

print(*ans)