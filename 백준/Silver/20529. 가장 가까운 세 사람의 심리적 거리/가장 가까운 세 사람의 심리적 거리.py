import sys
input = sys.stdin.readline
from itertools import combinations


def opr(a, b, c):

    tmp = 0
    for i in range(4):
        if a[i] != b[i]:
            tmp += 1
        if a[i] != c[i]:
            tmp += 1
        if b[i] != c[i]:
            tmp += 1

    return tmp

T = int(input())
for _ in range(T):
    N = int(input())
    mbti = input().rstrip().split(" ")
    if N > 32:
        print(0)
    else:
        ans = 12
        cnt = 0
        for combination in combinations(mbti, 3):
            ans = min(ans, opr(combination[0], combination[1], combination[2]))
        print(ans)
