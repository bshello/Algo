T = int(input())

for tc in range(T):
    sit = list()
    p, m = map(int, input().split())
    for i in range(p):
        n = int(input())
        if n not in sit:
            sit.append(n)
        else:
            pass
    ans = p - len(sit)
    print(ans)