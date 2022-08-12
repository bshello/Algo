tot =int(input())
price = []
s = 0

for i in range(9):
    price.append(int(input()))

for j in range(9):
    s += price[j]
ans = tot - s
print(ans)