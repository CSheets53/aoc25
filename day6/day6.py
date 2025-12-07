with open('day6.txt', 'r') as file:
    data = file.read().splitlines()

def part1():
    rows = [r.split() for r in data]
    operands = rows[:-1]
    operators = rows[-1]

    solutions = [0 if x == '+' else 1 for x in operators]
    for i in range(len(operands)):
        for j in range(len(operands[i])):
            if operators[j] == '+':
                solutions[j] += int(operands[i][j])
            else:
                solutions[j] *= int(operands[i][j])

    return sum(solutions)

print(f"Part 1: {part1()}")

def part2():
    rows = [r for r in data]
    operands = rows[:-1]
    operators = rows[-1]

    solutions = []
    current_operands = []
    current_operator = operators[0]
    for j in range(len(operands[0])):
        if j != 0 and operators[j] != ' ':
            # new operator, so finish last calculation
            new_solution = 0
            if current_operator == '+':
                new_solution = sum(current_operands)
            else:
                new_solution = 1
                for operand in current_operands:
                    new_solution *= operand
            
            solutions.append(new_solution)
            current_operands = []
            current_operator = operators[j]

        new_operand = ''
        for i in range(len(operands)):
            new_operand = new_operand + operands[i][j]
        
        # finished constructing new operand
        if new_operand.strip() != '':
            new_operand = int(new_operand)
            current_operands.append(new_operand)

    # handle last operation
    new_solution = 0
    if current_operator == '+':
        new_solution = sum(current_operands)
    else:
        new_solution = 1
        for operand in current_operands:
            new_solution *= operand
    
    solutions.append(new_solution)
    current_operands = []
    current_operator = operators[j]

    return sum(solutions)

print(f"Part 2: {part2()}")
