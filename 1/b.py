file = open('input', 'r')
sum = 0

for mass in file:
    while True:
        mass = int(mass) // 3 - 2
        if mass > 0:
            sum += mass
        else:
            break

print(sum)
