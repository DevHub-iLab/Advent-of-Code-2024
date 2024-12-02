# Requires https://pypi.org/project/advent-of-code-data/
import aocd as aoc

input = aoc.get_data(year=2024, day=1)

# Parse string input into sorted arrays
left = []
right = []
for line in input.split("\n"):
    num1, num2 = line.split("   ")
    left.append(int(num1))
    right.append(int(num2))

left.sort()
right.sort()

### Part 1
dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])
print("Part 1:")
print(dist)


###Part 2
from collections import Counter
freq_dict = Counter(right)
freq_dict = dict(freq_dict)

simscore = 0
for item in left:
    if item in freq_dict:
        simscore += item * freq_dict[item]
print("Part 2:")
print(simscore)