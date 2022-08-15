T = int(input())
for tc in range(T):
    n = int(input())
    park = list(map(int, input().split()))
    ma = 0
    mi = 100
    for i in park:
        if ma < i:
            ma = i
        if mi > i:
            mi = i
    ans = 2*(ma-mi)
    print(ans)