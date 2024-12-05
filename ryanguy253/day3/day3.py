day3 = open("resources/day3.txt")
data = day3.read()

print(f"Data : {data}")

'''
Part 1
'''
# Use Regex to find Mul(x,y)
import re

mul_instructions = re.findall(r"mul\(-?\d+,-?\d+\)",data)
print(f"\nMultiplication Instructions: {mul_instructions}")

multiplication_array = []

# Extract Digits from the mul_instructions
for instruction in mul_instructions:
    numbers = re.findall(r"-?\d+",instruction)
    numbers = [int(number) for number in numbers]
    multiplication_array.append(numbers)

print(f"\nMultiplication Array: {multiplication_array}")

total = 0

for mul in multiplication_array:
    total += mul[0]*mul[1]

print(total)

'''
Part 2
'''

print("\nPart 2 \n")

# Get Multiplication instructions with do and dont keywords
# mul\(-?\d+,-?\d+\)) - multiplication regex
# do\(\) - do keyword
# don't\(\)" - dont keyword

'''
(?:...):
This is a non-capturing group. It groups part of the regex without capturing the matched portion of the text, which can be useful if you want to group expressions without storing the match in a separate capture group. The main difference between (?:...) and (...) is that the latter captures the match, while the former does not.

%s:
This is a string formatting placeholder in Python. It is replaced by the test_list when the code runs. So, '%s' % ... will insert the value of test_list into the string, which could be a list of individual regex patterns. The join method is used to join those individual patterns with a pipe |, which acts as the logical "OR" operator in regex.

'|'.join(test_list):
This takes all the items in the test_list and concatenates them into a single string, with each item separated by the pipe (|), which represents the logical OR in regular expressions. For example, if test_list = ['foo', 'bar', 'baz'], this would result in the string 'foo|bar|baz'.

https://www.geeksforgeeks.org/python-check-if-string-matches-regex-list/
'''

pattern = r"do\(\)|don't\(\)|mul\(-?\d+,-?\d+\)"
instructions = re.findall(pattern,data)

print(f"Instructions Array : {instructions}")
multiplication_instructions = []

skip = False

for instruction in instructions:
    if instruction == "do()":
        skip = False
    elif instruction == "don't()":
        skip = True
    if skip:
        continue
    elif not skip and instruction!="do()" and instruction!="don't()":
        multiplication_instructions.append(instruction)


multiplication_array = []
# Extract Digits from the mul_instructions
for instruction in multiplication_instructions:
    numbers = re.findall(r"-?\d+",instruction)
    numbers = [int(number) for number in numbers]
    multiplication_array.append(numbers)

total = 0

for mul in multiplication_array:
    total += mul[0]*mul[1]

print(total)