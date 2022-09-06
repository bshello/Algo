n = int(input())
m = list(map(int, input().split()))
m.sort()
if n % 2 == 1:
    ans = m[n//2]
else:
    temp = 0
    temp2 = 0
    for i in m:
        temp += abs(i - m[n//2])
        temp2 += abs(i - m[n//2 - 1])

    if temp >= temp2:
        ans = m[n // 2 - 1]
    else:
        ans = m[n // 2]

print(ans)