cnt = 0
score = 0
T = int(input())
for tc in range(T):
    a = list(input())
    for i in a:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0

    print(score)
    score = 0
    cnt = 0
