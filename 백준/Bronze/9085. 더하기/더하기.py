T = int(input())
for tc in range(T):
    s = 0
    n = int(input())
    num = list(map(int, input().split()))
    for i in num:
        s += i
    print(s)