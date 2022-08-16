alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
place = list()
for _ in range(26):
  place.append(-1)

sen = input()
temp = dict()
for i in range(len(sen)):
  for j in range(len(alpha)):
    if sen[i] == alpha[j]:
      if place[j] == -1:
        place[j] += i+1
print(*place)