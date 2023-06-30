import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    opr = input().rstrip()
    n = int(input())
    num = input().rstrip()[1:-1].split(",")
    reverse = False
    start = 0
    end = n
    for c in opr:
        if c == "R":
            reverse = not reverse
        else:
            if start >= end:
                print("error")
                break
            if reverse:
                end -= 1
            else:
                start += 1
    else:
        ans = num[start:end]
        if reverse:
            ans = ans[::-1]
        answer = "[" + ",".join(ans) + "]"
        print(answer)