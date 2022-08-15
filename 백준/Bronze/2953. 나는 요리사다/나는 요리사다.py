T = 5
com = list()
for tc in range(T):
    s = 0
    score = list(map(int, input().split()))
    for i in score:
        s += i
    com.append(s)
temp = 0
idx = list()
for j in range(5):
    if temp < com[j]:
        temp = com[j]
        idx.append(j)
ans = idx[-1]+1
print(ans, temp)
