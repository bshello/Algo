n = int(input())
pick = list(map(int, input().split()))
line = [1]
if n > 1:
    for i in range(1, n):
        temp = []
        for j in range(pick[i]):
            temp.append(line.pop())
        line.append(i+1)
        for k in range(pick[i]):
            line.append(temp.pop())

print(*line)
