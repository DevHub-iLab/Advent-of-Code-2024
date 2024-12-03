import re
f = open("/workspaces/Advent-of-Code-2024/emily7lim/day3/data.txt", "r")
contents = f.read()
mulregex = "mul\((\d+)\,(\d+)\)"
def int_sum(spec):
    inti = []
    for i in spec:
        inti.append(tuple(map(int,i)))

    totalsum = sum(x*y for (x,y) in inti)
    return totalsum

#part1
spec = re.findall(mulregex,contents)
print(int_sum(spec))

#part2
docontent = contents.split("do()")
if "don't()" in docontent[0]:
    selected = docontent[0].split("don't()")[0]
else:
    selected = docontent[0]

for i in docontent[1:]:
    if "don't()" in i:
        removed = i.split("don't()")[0]
        selected += removed
    else:
        selected += i

spec=re.findall(mulregex,selected)
print(int_sum(spec))
