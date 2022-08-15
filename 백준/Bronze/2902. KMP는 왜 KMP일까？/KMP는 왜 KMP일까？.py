text = list(input())
temp = [text[0]]
for i in range(1, len(text)):
    if text[i-1] == '-':
        temp.append(text[i])
ans = ''
for j in temp:
    ans += j
print(ans)