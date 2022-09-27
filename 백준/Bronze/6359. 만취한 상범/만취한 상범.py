for tc in range(1, int(input())+1):
    round = int(input())
    arr = [0] * (round+1)
    for i in range(1, round+1):
        for j in range(i,round+1,i):
            if arr[j] == 0:
                arr[j] = 1
            else:
                arr[j] = 0
    cnt = 0
    for i in range(1, round+1):
        if arr[i] == 1:
            cnt += 1

    print(cnt)