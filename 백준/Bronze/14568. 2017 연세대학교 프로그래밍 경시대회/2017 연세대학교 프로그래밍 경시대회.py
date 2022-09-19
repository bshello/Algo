n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(n+1-i):
        a = i
        b = j
        c = n-(i+j)
        if a > 0 and b > 0 and c > 0 and c > b + 1 and a % 2 == 0:
            cnt += 1


print(cnt)