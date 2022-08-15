yut = list()
for tc in range(3):
    n = list(map(int, (input().split())))
    cnt = 0
    for i in n:
        if i % 2 == 0:
            cnt += 1

    if cnt == 1:
        cnt = 'A'
    elif cnt == 2:
        cnt = 'B'
    elif cnt == 3:
        cnt = 'C'
    elif cnt == 4:
        cnt = 'D'
    else:
        cnt = 'E'

    print(cnt)