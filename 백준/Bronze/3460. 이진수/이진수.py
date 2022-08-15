T = int(input())
for tc in range(T):
    num = int(input())
    ans = list()
    cnt = 0

    while True:
        if num <= 0:
            break
        if num % 2 == 1:
            ans.append(cnt)

        num //= 2
        cnt += 1

    for i in ans:
        print(i, end=" ")