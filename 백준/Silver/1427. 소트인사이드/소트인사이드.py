n = list(input())
n.sort(reverse=True)
ans = ''
for i in n:
    ans += i
print(ans)