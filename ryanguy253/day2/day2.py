day2 = open("resources/day2.txt", "r")
data = day2.read()
array = data.split("\n")

data = []
for i in array:
    j = i.split(" ")
    j = [int(x) for x in j]
    data.append(j)

print(f"Data : {data}")

'''
Safe Meaning
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
'''

def is_safe(diffs):
    #Check if the given differences array is safe
    all_increasing = all(1 <= d <= 3 for d in diffs)
    all_decreasing = all(-3 <= d <= -1 for d in diffs)
    return all_increasing or all_decreasing

def is_safe_with_dampener(levels):
    #Check if removing one level makes the sequence safe.
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        diffs = [modified_levels[j] - modified_levels[j - 1] for j in range(1, len(modified_levels))]
        if is_safe(diffs):
            return True
    return False


count = 0
for report in data:
    # Compute the difference array
    diffs = [report[j] - report[j - 1] for j in range(1, len(report))]

    if is_safe(diffs):
        count += 1

    elif is_safe_with_dampener(report):
        count += 1

print(f"Total safe: {count}")



'''
for i in data:
    increasing = False
    chances = 0

    diff = i[1] - i[0]
    # Check for increasing/decreasing
    if diff > 0:
        increasing = True
    else:
        increasing = False

    # For loop
    for j in range(1, len(i)):
        diff = i[j] - i[j - 1]
        # Check for increasing/decreasing
        if diff > 0:
            if not increasing:
                    break

        else: # Diff<0
            if increasing:
                    break


        # Check for diff > 3 or diff = 0
        if abs(diff) > 3 or diff==0:
                break

        if(j == len(i)-1) : count+=1

print(count)
'''
