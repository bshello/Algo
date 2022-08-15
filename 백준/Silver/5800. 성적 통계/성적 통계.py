T = int(input())
for tc in range(T):
    n = list(map(int, input().split()))
    m = n[0]
    del n[0]
    ma = 0
    mi = 100
    for i in n:
        if ma < i:
            ma = i
        if mi > i:
            mi = i
    temp = list()
    n.sort()
    for j in range(1,m):
        a = 0
        if n[j-1] > n[j]:
            a = n[j-1] - n[j]
            temp.append(a)
        else:
            a = n[j] - n[j-1]
            temp.append(a)
    temp.sort()
    print(f'Class {tc+1}')
    print(f'Max {ma}, Min {mi}, Largest gap {temp[-1]}')