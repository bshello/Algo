T = int(input())
for tc in range(T):
    N = int(input())
    al = list()
    bl = list()
    temp = list()
    asum = 0
    tsum = 0

    for i in range(N):
        a, b = map(float, input().split())
        al.append(a)
        bl.append(b)

    for j in range(N):
        asum+=al[j]

    for k in range(N):
        temp.append(al[k]*bl[k])
        tsum += temp[k]
    avg = tsum/asum
    print(f'{int(asum)} {avg:.1f}')
