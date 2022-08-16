alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
place = list()
for _ in range(26):
  place.append(0)

sen = input()
temp = dict()
for i in sen:
  for j in range(len(alpha)):
    if i == alpha[j]:
      place[j] += 1
print(*place)