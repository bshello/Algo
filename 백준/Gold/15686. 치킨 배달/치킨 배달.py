from collections import deque
def dfs(num):
    if len(temp) == M:
        tes = temp.copy()
        Q.append(tes)
        return

    for i in range(num, len(chicken)):
        r, c = chicken[i]
        if (r, c) not in temp:
            temp.append((r, c))
            dfs(i)
            temp.pop()

N, M = map(int, input().split())
chicken = []
house = []
Q = deque()
temp = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            house.append((i, j))
        elif tmp[j] == 2:
            chicken.append((i, j))

dfs(0)
ans = 0xffffff
while Q:
    chick = Q.popleft()
    s = 0
    for i in range(len(house)):
        minn = 0xffffff
        for j in range(M):
            minn = min(minn, abs(house[i][0] - chick[j][0]) + abs(house[i][1] - chick[j][1]))
        s += minn
    ans = min(ans, s)

print(ans)