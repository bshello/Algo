n = input()
cnt = 0
for i in n:
    if cnt == 10:
        cnt = 0
        print('')
        print(i, end='')
    else:
        print(i, end='')
    cnt += 1