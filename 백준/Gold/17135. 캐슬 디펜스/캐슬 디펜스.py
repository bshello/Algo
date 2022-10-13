from itertools import combinations
from collections import deque

N, M, D = map(int, input().split())
qenemy = deque()
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M-1, -1, -1):
        if temp[j] == 1:
            qenemy.append((i, j))

temp = []
for i in range(M):
    temp.append(i)
tmp = combinations(temp, 3)
bowman = deque()
for i in tmp:
    bowman.append(i)
ans = 0
while bowman:
    one, two, three = bowman.popleft()
    enemy = qenemy.copy()
    cnt = 0
    while enemy:
        temp = deque()
        oned = 0xffffff
        oneidx = (N + 1, M + 1)
        twod = 0xffffff
        twoidx = (N + 1, M + 1)
        trdd = 0xffffff
        trdidx = (N + 1, M + 1)
        while enemy:
            r, c = enemy.pop()
            fd = abs(N - r) + abs(one - c)
            sd = abs(N - r) + abs(two - c)
            td = abs(N - r) + abs(three - c)
            if fd <= D and fd <= oned:
                if fd == oned:
                    if oneidx[1] > c:
                        oneidx = (r, c)
                else:
                    oneidx = (r, c)
                    oned = fd

            if sd <= D and sd <= twod:
                if sd == twod:
                    if twoidx[1] > c:
                        twoidx = (r, c)
                else:
                    twoidx = (r, c)
                    twod = sd
            if td <= D and td <= trdd:
                if td == trdd:
                    if trdidx[1] > c:
                        trdidx = (r, c)
                else:
                    trdidx = (r, c)
                    trdd = td
            temp.append((r, c))
        while temp:
            r, c = temp.popleft()
            if (r, c) == oneidx or (r, c) == twoidx or (r, c) == trdidx:
                cnt += 1
            else:
                if r + 1 < N:
                    enemy.append((r + 1, c))

    ans = max(ans, cnt)

print(ans)
