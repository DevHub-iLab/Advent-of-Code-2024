##path in codespace
f = open("/workspaces/Advent-of-Code-2024/emily7lim/day2/data.txt", "r")
contents = f.read().split("\n")

pdiff = [1,2,3]
ndiff = [-1,-2,-3]
def valid(lines):
    for j in range(len(lines)):
        if j+1 == len(lines):
            break
        diff = int(lines[j]) - int(lines[j+1])
        if j == 0:
            prevsign = diff
        if diff in pdiff and prevsign>0:
            prevsign = diff
            safe = True
        elif diff in ndiff and prevsign<0:
            prevsign = diff
            safe = True
        else:
            return False
    return safe

count=0

#part1
for i in contents:
    lines = i.split()
    if valid(lines):
        count+=1
print(count)

#part2    
count = 0
for i in contents:
    lines = i.split()
    if valid(lines):
        count+=1
    else:
        for j in range(len(lines)):
            newlines = lines.copy()
            del newlines[j]
            if valid(newlines):
                count+=1
                break
print(count)
            