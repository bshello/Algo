import sys
input = sys.stdin.readline
first = input().rstrip()
second = input().rstrip()

f = len(first)
s = len(second)
chart = [[0] * (s + 1) for _ in range(f + 1)]

for i in range(f):
    for j in range(s):
        if first[i] == second[j]:
            chart[i + 1][j + 1] = chart[i][j] + 1
        else:
            chart[i + 1][j + 1] = max(chart[i + 1][j], chart[i][j + 1])

print(chart[-1][-1])
