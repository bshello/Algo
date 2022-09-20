n = int(input())
num = list(map(int, input().split()))
ans = n
if 1 in num:
    ans -= 1
for i in range(n):
    for j in range(2, int(num[i]**(1/2))+1):
        if num[i] % j == 0:
            ans -= 1
            break

print(ans)