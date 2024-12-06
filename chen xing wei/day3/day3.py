import re
file = open("day3.txt", 'r')
ans1 = 0
regex1 = r"mul\((\d+),(\d+)\)" #only extract numbers that matches pattern
for line in file:
    match = re.findall(regex1, line)
    for i in match:
        ans1 += int(i[0]) * int(i[1])
print(ans1)
file.close()


file = open("day3.txt", 'r')
ans2 = 0
regex2 = r"mul\(\d+\.?\d*,\d+\.?\d*\)|do\(\)|don't\(\)" #extract mul() || do() || don't() from data
state = True #used to track if last command is 0 or 1
for line in file:
    match = re.findall(regex2, line)
    for i in match:
        if i == "don't()":
            state = False
        elif i == "do()":
            state = True
        else:
            if state:
                firstHalf, secHalf = i.split(",") #split into "mul(x" and "y)"
                num1 = int(firstHalf.split("(")[1])
                num2 = int(secHalf.split(")")[0])
                ans2 += num1 * num2
print(ans2)
file.close()