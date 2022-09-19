n = int(input())
cnt = 0
for i in range(1,500):
    a = (i ** 2 + n)**(1/2)

    if a % 1 == 0 and a <= 500:
        cnt += 1

print(cnt)