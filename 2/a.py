def compute(instructions):
    ADD = 1
    MULTIPLY = 2
    INTERRUPT = 99
    for i in range(0, len(instructions), 4):
        instruction = instructions[i]
        if instruction == INTERRUPT:
            break

        a = instructions[i+1]
        b = instructions[i+2]
        out = instructions[i+3]

        if instruction == ADD:
            instructions[out] = instructions[a] + instructions[b]
        elif instruction == MULTIPLY:
            instructions[out] = instructions[a] * instructions[b]

    return instructions[0]


def get_instructions():
    with open('input') as f:
        instructions = f.readline().rstrip().split(',')
        return list(map(int, instructions))


if __name__ == "__main__":
    print(compute(get_instructions()))
