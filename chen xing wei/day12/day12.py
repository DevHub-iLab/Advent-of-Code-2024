file = open("day12\day12.txt", 'r')
farm = {}
ans1 = 0

def getInput():
    for y, i in enumerate(file):
        line = list(i.strip())
        for x in range(len(line)):
            if(line[x] in farm):
                farm[line[x]].append([y, x])
            else:
                farm[line[x]] = [[y, x]]

def findRegion(plant):
    startPos = plant.pop()
    region = [startPos]
    stack = [startPos]
    dirs = ((1,0), (-1,0), (0,1), (0,-1))
    while(len(stack) != 0): #for finding region
        currPos = stack.pop()
        x, y = currPos[1], currPos[0]
        for diffX, diffY in dirs:
            if([y+diffY,x+diffX] in plant):
                region.append([y+diffY,x+diffX])
                stack.append([y+diffY,x+diffX])
                plant.remove([y+diffY,x+diffX])

    negPerimeter = 0
    for pos in region: #for finding negPerimeter
        x, y = pos[1], pos[0]
        for diffX, diffY in dirs:
            if([y+diffY, x+diffX] in region): #check all 4 dirs and -- if theres smth in the dir
                negPerimeter += 1
    return len(region), len(region)*4 - negPerimeter

getInput()
for key, value in farm.items():
    plant = value
    while(len(plant) != 0):
        area, perimeter = findRegion(plant)
        ans1 += area*perimeter
print("Part 1:", ans1)