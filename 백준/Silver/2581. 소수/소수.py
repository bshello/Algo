import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
s = 0
ans = list()
for i in range(m,n+1):
    cnt = 0
    for j in range(2,i+1):
        if i%j == 0:
            cnt+=1
    if cnt == 1:
        s+=i
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    print(s)
    print(ans[0])
