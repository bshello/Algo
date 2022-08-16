n = list(input())
temp = list()
for i in n:
    j = ord(i)
    if j >= 65 and j <= 90:
        j += 13
        if j >90:
            j-= 26
    elif j>= 97 and j <= 122:
        j += 13
        if j >122:
            j-= 26
    else:
        pass
    temp.append(chr(j))

ans = ''.join(temp)

print(ans)