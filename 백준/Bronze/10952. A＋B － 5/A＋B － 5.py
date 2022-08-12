while True:
    n, m = map(int, input().split())
    if n == 0:
        if m == 0:
            break
    ans = n+m
    print(ans)