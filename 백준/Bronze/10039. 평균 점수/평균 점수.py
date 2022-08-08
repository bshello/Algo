score = list()
sum = 0
for i in range(5):
    a = int(input())
    score.append(a)
for j in range(len(score)):
    if score[j] < 40:
        score[j] = 40
    sum += score[j]
avg = int(sum/len(score))
print(avg)