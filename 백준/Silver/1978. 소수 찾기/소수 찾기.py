N = int(input())
num = list(map(int, input().split()))
ans = 0
for i in num:
    for j in range(N):
        cnt = 0
        if num[j]>2:
            for k in range(1,num[j]):
                if num[j] % k != 0:
                    cnt+=1
                    if cnt == num[j]-2:
                        ans+=1

answer = int(ans/N)
if 2 in num:
    answer+=1

print(answer)
