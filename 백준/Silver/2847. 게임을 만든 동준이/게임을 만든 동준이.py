n = int(input())
inp = [int(input()) for _ in range(n)]
i = n-2
cnt = 0

while i >= 0:
    while True:
        if inp[i] >= inp[i+1]:
            inp[i] -= 1
            cnt += 1
        else:
            break
    i -= 1

print(cnt)