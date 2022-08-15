n = int(input())
temp = 1
for i in range(1, n+1):
    temp *= i
ans = list(str(temp))
ans.reverse()
answer = list()
cnt = 0
for j in range(len(ans)):
    cnt +=1
    if ans[j] != '0':
        break
print(cnt-1)
