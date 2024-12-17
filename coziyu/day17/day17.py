import aocd
input = aocd.get_data(day=17, year=2024)

# input = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

# input = """Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0"""

### Part 1 - Straightforward simulation 
import re
def parse(input):
    registers, program = input.split("\n\n")
    pattern = r"(\d+)"
    match = re.findall(pattern, registers)
    registers = {4: int(match[0]), 5: int(match[1]), 6: int(match[2])}

    patternP = r"Program: (.+)"
    program = re.match(patternP, program).group(1)
    program = program.split(",")
    program = [int(x) for x in program]
    return registers, program

def get_combo_operand(registers, combo_operand):
    if combo_operand < 4:
        return combo_operand
    return registers[combo_operand]

def simulate(registers, program, pc, opcode, operand):
    out = []
    while pc < len(program):
        opcode = program[pc]
        operand = program[pc + 1]
        pc += 2
        #adv
        if opcode == 0:
            numer = registers[4]
            denom = pow(2, get_combo_operand(registers, operand))
            registers[4] = numer // denom
        #bxl
        if opcode == 1:
            registers[5] = registers[5] ^ operand
        #bst
        if opcode == 2:
            registers[5] = get_combo_operand(registers, operand) % 8
        #jnz
        if opcode == 3:
            if registers[4] != 0:
                pc = operand
        #bxc
        if opcode == 4:
            registers[5] = registers[5] ^ registers[6]
        #out
        if opcode == 5:
            to_output = get_combo_operand(registers, operand) % 8
            out.append(to_output)
        #bdv
        if opcode == 6:
            numer = registers[4]
            denom = pow(2, get_combo_operand(registers, operand))
            registers[5] = numer // denom
        #cdv
        if opcode == 7:
            numer = registers[4]
            denom = pow(2, get_combo_operand(registers, operand))
            registers[6] = numer // denom
    return out

registers, program = parse(input)
# print(registers)
# print(program)
out = simulate(registers, program, 0, 0, 0)
print(",".join([str(o) for o in out]))

### Part 2 - Decompilation and reverse engineering
# Upon manually decompiling my given program:
# 1. B = A % 8
# 2. B = B ^ 1
# 3. C = A >> B
# 4. B = B ^ 5
# 5. B = B ^ C
# 6. A = A >> 3
# 7. OUT B % 8
# 8. IF A != 0, GOTO 1
#
# I noticed that in each iteration,
# the values of B and C are initialised solely based on A.
# This means that values of B and C are somewhat 
# independent of the iteration, we just need to know what A is
# in every iteration. Conveniently, A is bitshifted rightwards by 3
# between every iteration. 
#
# This told me that, the each value of output of the program 
# is dependent on single 3 bit blocks in the binary 
# representation of A. Each 3 bit block independently 
# (but non uniquely) determines the output of the program.
#
# Thus, we can iteratively find the value of A by finding the 
# 3 bit blocks that results in the output values.

def initialise(a, registers):
    registers[4] = a
    registers[5] = 0
    registers[6] = 0

# On the ith iteration, we find the A value that matches 
# up to the ith character from the end of the program
count = 1
i = 1
while True:
    # Increment i by 1 until ith character from the end matches.
    initialise(i, registers)
    out = simulate(registers, program, 0, 0, 0)
    if out[-count] == program[-count]:
        # print(i)
        # print(out)
        # print(program)
        count += 1
        if count - 1 == len(program):
            # weird edge case
            if out == program:
                break
            else:
                count -= 1
                i += 1
        else:
            i *= 8
    else:
        i += 1

print(i)