import aocd as aoc
input = aoc.get_data(year=2024, day=2)

# Parse input into report array
lines = input.split("\n")
reports = []
for line in lines:
    arr = line.split(" ")
    arr = [int(r) for r in arr]
    reports.append(arr)

# Part 1 Helper Functions
# A slow 3 pass approach suffices
def is_decreasing(report):
    for i in range(len(report)):
        if i < len(report) - 1:
            if report[i] <= report[i+1]:
                return False
    return True
def is_increasing(report):
    for i in range(len(report)):
        if i < len(report) - 1:
            if report[i] >= report[i+1]:
                return False
    return True
def is_capped(report):
    for i in range(len(report)):
        if i < len(report) - 1:
            if abs(report[i] - report[i+1]) >= 4:
                return False
    return True

def is_strictly_monotonic(report):
    return is_decreasing(report) or is_increasing(report)

def is_safe(report):
    return is_strictly_monotonic(report) and (is_capped(report))

### Part 1:
safe_count = 0
for report in reports:
    if is_safe(report):
        safe_count += 1
print("Part 1:")
print(safe_count)

### Part 2:
def is_safe_with_removal(report):
    if is_safe(report):
        return True
    # Try removing at index j
    for j in range(len(report)):
        reportA = report.copy()
        del reportA[j]
        if is_safe(reportA):
            return True
    return False

safe_count_with_rem = 0
for report in reports:
    if is_safe_with_removal(report):
        safe_count_with_rem += 1
print("Part 2:")
print(safe_count_with_rem)