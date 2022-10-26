def solve(depth):
    if depth == n:
        print(*arr)
        return
    for i in range(m):
        if depth > 0:
            if ml[i] >= arr[depth - 1]:
                arr[depth] = ml[i]
                solve(depth + 1)
        else:
            arr[depth] = ml[i]
            solve(depth + 1)


m, n = map(int, input().split())
arr = [0] * n
ml = list(map(int, input().split()))
ml.sort()
solve(0)