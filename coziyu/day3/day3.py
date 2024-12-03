import aocd as aoc
input = aoc.get_data(year=2024, day=3)
test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

### Part 1
# A simple regex pattern capturing the operands of mul() suffices
import re
mul_pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(mul_pattern, input)

total_sum = sum(int(x) * int(y) for x, y in matches)
print(total_sum)


### Part 2
# We now need to keep track of the enabled state of mul instructions
# So a loop through all matches in sequence is necessary
control_pattern = r"(do\(\)|don't\(\))"
match_seq = re.finditer(f"{mul_pattern}|{control_pattern}", input)

enabled = True 
total_sum_do = 0

for match in match_seq:
    if match.group(0).startswith("mul"):
        if enabled:
            x, y = match.groups()[0:2]
            total_sum_do += int(x) * int(y)
    elif match.group(0) == "do()":
        enabled = True
    elif match.group(0) == "don't()":
        enabled = False
    else:
        print("Unexpected match")
        print(match.group(0))

print(total_sum_do)