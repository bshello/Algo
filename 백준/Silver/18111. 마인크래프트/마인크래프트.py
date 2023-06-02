import sys

def craft(height, Block):
    global answer, ansHeight
    ans = 0
    check = True

    for i in range(N):
        for j in range(M):
            temp = arr[i][j] - height
            if temp > 0:
                Block += 1 * temp
                ans += 2 * temp
            elif temp < 0:
                Block -= 1 * abs(temp)
                ans += 1 * abs(temp)
            if ans > answer:
                check = False
                break

    if check and Block >= 0:
        answer = ans
        ansHeight = height
    return

Max = - sys.maxsize
Min = sys.maxsize

N, M, B = map(int, input().split())
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    Max = max(Max, max(tmp))
    Min = min(Min, min(tmp))
    arr.append(tmp)

answer = sys.maxsize
ansHeight = - sys.maxsize
for height in range(Min, Max + 1):
    Block = B
    craft(height, Block)

print(answer, ansHeight)
