chip,num,money = map(int, input().split())
tot = chip*num
mom = tot - money
if mom<0:
    mom = 0
print(mom)