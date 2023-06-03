import sys
input = sys.stdin.readline
N = int(input())

people = list(map(int, input().split()))

people.sort()
s = 0
for i in range(N):
    s += (N - i) * people[i]

print(s)