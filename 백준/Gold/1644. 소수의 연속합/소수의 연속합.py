N = int(input())
if N < 2:
    print(0)
else:
    num = [True] * (N + 1)
    prime = []
    for i in range(2, N + 1):
        if num[i] == True:
            prime.append(i)
            for j in range(2 * i, N + 1, i):
                num[j] = False
    i = -1
    j = 0
    s = prime[0]
    ans = 0
    while True:
        if s < N:
            if j == len(prime) - 1:
                break
            j += 1
            s += prime[j]

        else:
            if s == N:
                ans += 1
            if j > i:
                i += 1
                s -= prime[i]
            else:
                if j < len(prime) - 1:
                    j += 1
                    s += prime[j]
                else:
                    break


    print(ans)