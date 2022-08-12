N = int(input())

for i in range((N*2)-1):
    if i < N:
        print(' '*(N-1-i) + '*'*((2*i)+1))
    else:
        j = i - N + 1
        print(' '*(j) + '*'*(((N * 2) - 1) - (2 * j)))