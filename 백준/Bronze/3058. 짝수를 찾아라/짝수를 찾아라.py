T = int(input())
for tc in range(T):
    n = list(map(int, input().split()))
    num = list()
    for i in n:
        if i%2 == 0:
            num.append(i)
    num.sort()
    s = 0
    for j in num:
        s += j
    print(s, num[0])