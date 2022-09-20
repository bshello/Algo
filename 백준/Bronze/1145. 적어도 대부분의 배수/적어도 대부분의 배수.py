num = list(map(int, input().split()))
num.sort()
m = 100 * 100 * 100
tmp = {}
ans = []
for i in range(5):
    for j in range(num[i], m+1, num[i]):
        if j not in tmp:
            tmp.update({j: 1})
        else:
            tmp[j] += 1
        if tmp[j] == 3:
            ans.append(j)

ans.sort()
print(ans[0])

