n = list(map(int, input().split()))
s = 0
for i in n:
    s += i**2
ans = s%10
print(ans)