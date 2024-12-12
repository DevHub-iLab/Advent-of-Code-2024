import re

with open("input.txt", "r") as f:
    pattern = r"mul\((\d+),(\d+)\)"
    ris = 0
    for line in f:
        matches = re.findall(pattern, line)
        for x, y in matches:
            ris += int(x) * int(y)

    print(ris)