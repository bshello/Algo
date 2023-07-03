import sys
input = sys.stdin.readline

N = int(input())
P_length = N * 2 + 1
M = int(input())
S = input().rstrip()

ans = 0
index = 0
while index <= M - P_length:

    if S[index] == "I":

        for j in range(P_length):
            if j % 2 == 0:
                if S[index + j] != "I":
                    break
            else:
                if S[index + j] != "O":
                    break
        else:
            ans += 1

    index += 1

print(ans)