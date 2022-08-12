T = int(input())
for tc in range(T):
    s = int(input())
    n = int(input())
    for op in range(n):
        q, p = map(int, input().split())
        a = q * p
        s += a
    print(s)