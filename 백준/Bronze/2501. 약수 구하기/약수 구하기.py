n, k = map(int, input().split())
ans = list()
for j in range(1,n+1):
    if n%j == 0:
        ans.append(j)
if len(ans) < k:
    print(0)
else:
    answer = ans[k-1]
    print(answer)