def solve(x):
    s = 0
    e = M - 1
    while s <= e:
        middle = (s + e)//2
        if x > mnum[middle]:
            s = middle + 1
        elif x < mnum[middle]:
            e = middle - 1
        else:
            ans[x] += 1
            return
    return

N = int(input())
nnum = list(map(int, input().split()))
M = int(input())
mnum = list(map(int, input().split()))
xnum = mnum.copy()
mnum.sort()
ans = dict()

for j in xnum:
    ans.update({j: 0})

for i in nnum:
    solve(i)

for j in xnum:
    print(ans[j], end=" ")