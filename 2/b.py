from a import compute, get_instructions

TARGET = 19690720
instructions = get_instructions()

for i in range(1, 99):
    for j in range(1, 99):
        copy = instructions[:]
        copy[1] = i
        copy[2] = j
        try:
            ans = compute(copy)
            if ans == TARGET:
                print(100 * i + j)
        except IndexError:
            pass
