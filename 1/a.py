file = open('input', 'r')
sum = 0

for mass in file:
    fuel = int(mass) // 3 - 2
    if fuel > 0:
        sum += fuel

print(sum)
