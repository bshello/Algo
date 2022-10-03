def dfs(n):
    global cnt
    if len(network[n]) == 0:
        return

    for i in network[n]:
        if not visited[i]:
            visited[i] = 1
            if i != 1:
                cnt += 1
            dfs(i)

Com = int(input())
N = int(input())
network = [[] for _ in range(Com + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
visited = [0] * (Com + 1)
cnt = 0
dfs(1)
print(cnt)
