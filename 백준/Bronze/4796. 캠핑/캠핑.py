res = []
cnt = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    temp = v // p
    temp2 = v % p
    ans = temp * l
    if temp2 > l:
        ans2 = l
    else:
        ans2 = temp2
    answer = ans + ans2
    res.append(answer)
    cnt += 1

for i in range(1, cnt):
    print(f'Case {i}: {res[i-1]}')
