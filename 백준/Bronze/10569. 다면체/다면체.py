T = int(input())
for tc in range(T):
    v, e = map(int, input().split())
    ans = e-v+2
    print(ans)