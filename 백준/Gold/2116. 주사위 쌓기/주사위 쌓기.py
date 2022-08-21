t = int(input())
dice = list()
for _ in range(t):
    n = list(map(int, input().split()))
    dic = [n[0],n[1],n[2],n[4],n[3],n[5]]
    dice.append(dic)

i = 0
cnt = 0
ans = 0
tt = list()
ttt = list()
while i<6:

    temp = 0
    templ = list()
    templ.append(dice[0][i])
    templ.append(dice[0][5-i])

    ttt.append(templ)
    if 6 not in templ:
        temp += 6
    elif 5 not in templ:
        temp += 5
    else:
        temp += 4

    for j in range(t-1):
        for k in range(6):
            if dice[j][5-i] == dice[j+1][k]:
                break
        i = k
        templ = list()
        templ.append(dice[j+1][i])
        templ.append(dice[j+1][5 - i])
        ttt.append(templ)
        if 6 not in templ:
            temp += 6
        elif 5 not in templ:
            temp += 5
        else:
            temp += 4
    tt.append(temp)
    cnt += 1
    i = cnt
    if ans < temp:
        ans = temp

print(ans)