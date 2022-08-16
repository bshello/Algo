n = list(input())
temp = list()
for i in n:
    j = ord(i)
    if j <= 90:
        j += 32
    else:
        j -= 32
    temp.append(chr(j))

ans = ''.join(temp)
print(ans)