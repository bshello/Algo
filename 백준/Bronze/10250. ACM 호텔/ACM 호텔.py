for tc in range(1, int(input())+1):
    H, W, N = map(int, input().split())

    i = 1
    while N > H:
        N -= H
        i += 1


    if i < 10:
        print(f'{N}0{i}')
    else:
        print(f'{N}{i}')
