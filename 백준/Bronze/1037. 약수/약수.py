n = int(input())
num = list(map(int, input().split()))
num.sort()
if n == 1:
    ans = num[0]**2
else:
    ans = num[0] * num[-1]

print(ans)