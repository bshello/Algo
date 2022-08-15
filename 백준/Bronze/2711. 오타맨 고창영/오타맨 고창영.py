T = int(input())
for tc in range(T):
    n, st = map(str, input().split())
    m = int(n)
    sen = list(st)
    sen[m-1] = ''
    ans = ''
    for i in sen:
        ans += i
    print(ans)