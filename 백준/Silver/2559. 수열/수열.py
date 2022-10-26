n, m = map(int, input().split())
inp = list(map(int, input().split()))

temp = 0
for i in range(m):
    temp += inp[i]

ans = temp
for j in range(1,n-m+1):
    temp = temp - inp[j-1] + inp[j+m-1]
    if ans < temp:
        ans = temp

print(ans)