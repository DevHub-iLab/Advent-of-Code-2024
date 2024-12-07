import aocd

input = aocd.get_data(year=2024, day=7)

input = input.split("\n")
equations = []

for line in input:
    target, operands = line.split(': ')
    target = int(target)
    operands =list(map(int, operands.split(" ")))
    equations.append((target, operands))

### Part 1
def evaluate(operands, operators):
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += operands[i + 1]
        elif operators[i] == '*':
            result *= operands[i + 1]
        # For Part 2
        elif operators[i] == '|':
            # concatenate the next number
            result = int(str(result) + str(operands[i + 1]))
    return result

from itertools import product
def calibration_value(equation):

    target, operands = equation[0], equation[1]

    # Generate operator sequences
    num_operators = len(operands) - 1
    for ops in product('+*', repeat=num_operators):
        if evaluate(operands, ops) == target:
            return target
        
    return 0

sum1 = 0
for equation in equations:
    sum1 += calibration_value(equation)
print(sum1)

### Part 2. we just need to add a new operator for concatenation '|'
def calibration_value2(equation):
    target, operands = equation[0], equation[1]

    num_operators = len(operands) - 1
    for ops in product('+*|', repeat=num_operators):
        if evaluate(operands, ops) == target:
            return target
        
    return 0

sum2 = 0
for equation in equations:
    sum2 += calibration_value2(equation)
print(sum2)