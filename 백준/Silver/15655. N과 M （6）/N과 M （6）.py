def solve(depth):
    if depth == n:
        print(*arr)
        return
    for i in range(m):
        if vis[i] == 1:
            continue
        if depth > 0:
            if ml[i] >= arr[depth - 1]:
                arr[depth] = ml[i]
                vis[i] = 1
                solve(depth + 1)
                vis[i] = 0
        else:
            arr[depth] = ml[i]
            vis[i] = 1
            solve(depth + 1)
            vis[i] = 0


m, n = map(int, input().split())
arr = [0] * n
vis = [0] * m
ml = list(map(int, input().split()))
ml.sort()
solve(0)
