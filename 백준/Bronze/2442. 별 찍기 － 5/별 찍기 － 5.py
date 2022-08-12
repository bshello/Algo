N = int(input())
star = list()
for i in range(N):
    star.append(' ' * (N - i-1)+'*'*(2*i + 1))
for j in range(N):
    print(star[j])