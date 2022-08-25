n, m = map(int, input().split())
female = {}
male = {}
for _ in range(n):
    s, g = map(int, input().split())
    if s == 0:
        if g not in female:
            female.update({g : 1})
        else:
            female[g] += 1
    else:
        if g not in male:
            male.update({g : 1})
        else:
            male[g] += 1
s = 0
for key, value in female.items():
    if value%m == 0:
        s += value//m
    else:
        s += (value//m) + 1
for key, value in male.items():
    if value % m == 0:
        s += value // m
    else:
        s += (value // m) + 1

print(s)