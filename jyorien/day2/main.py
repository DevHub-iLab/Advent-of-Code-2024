reports = []
with open("day2.txt", "r") as file:
    for line in file:
        strs = line.split(" ")
        ints = [int(x) for x in strs]
        reports.append(ints)

print(reports[0])
safeCount = 0

def isValidLine(line):
    descending = False
    if line[0] - line[1] > 0:
        descending = True
    isValid = True
    for i in range(1, len(line)):
        # descending
        if descending:
            if not (line[i-1] - line[i] > 0 and line[i-1] - line[i] <= 3):
                isValid = False
                break
        # ascending
        else:
            if not (line[i-1] - line[i] < 0 and line[i-1] - line[i] >= -3):
                isValid = False
                break
    return isValid

for line in reports:
    
    isValid = isValidLine(line)

    if isValid:
        safeCount += 1
    else:
        isValidNow = False
        for i in range(len(line)):
            tmp = line[:i] + line[i+1:]
            isValidNow = isValidLine(tmp)
            if isValidNow:
                safeCount += 1
                break

print(safeCount)
            
