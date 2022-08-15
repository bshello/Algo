n = int(input())
score = list(map(int, input().split()))
base = 0
s = 0
for i in score:
    if base < i:
        base = i

for j in range(n):
    score[j] = (score[j]/base)*100
    s += score[j]

avg = s/n
print(avg)