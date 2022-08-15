n = int(input())
ox = list(map(int,input().split()))
temp = 0
score = 0
for i in range(n):
    if ox[i] == 1:
        temp += 1
    else:
        temp = 0
    score += temp
print(score)
