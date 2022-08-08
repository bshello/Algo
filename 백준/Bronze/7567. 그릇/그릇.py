plate = list(input())
h = 10
for i in range(1,len(plate)):
    if plate[i] == plate[i-1]:
        h+=5
    else:
        h+=10
print(h)