import sys

input = sys.stdin.readline
N = int(input())
S = set()
for _ in range(N):
    command = input()

    if command[0] == "a":
        if command[1] == "d":
            num = int(command[4:])
            S.add(num)
        else:
            S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif command[0] == "r":
        num = int(command[7:])
        if num in S:
            S.remove(num)
    elif command[0] == "c":
        num = int(command[6:])
        if num in S:
            print(1)
        else:
            print(0)
    elif command[0] == "t":
        num = int(command[7:])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif command[0] == "e":
        S = set()

