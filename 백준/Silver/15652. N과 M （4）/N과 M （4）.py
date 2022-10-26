def solve(depth):
    if depth == n:
        print(*arr)
        return
    for i in range(m):
        if depth > 0:
            if i + 1 >= arr[depth - 1]:
                arr[depth] = i + 1
                solve(depth + 1)
        else:
            arr[depth] = i + 1
            solve(depth + 1)


m, n = map(int, input().split())
arr = [0] * n

solve(0)