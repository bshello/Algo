def dfs(a, b):
    global ans
    if a > 10:
        if visited == [1] * 11:
            ans = max(ans, b)
        return

    for i in range(11):
        if not visited[i] and squad[a][i]:
            visited[i] = 1
            dfs(a+1, b + squad[a][i])
            visited[i] = 0
            
for tc in range(int(input())):
    squad = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    ans = 0
    dfs(0, 0)
    print(ans)