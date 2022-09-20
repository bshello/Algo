m, n = map(int, input().split())
arr = [True] * (n+1)
prime = []
for i in range(n+1):
    if i == 0 or i == 1:
        continue
    elif arr[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            arr[j] = False

for k in prime:
    if k >= m:
        print(k)