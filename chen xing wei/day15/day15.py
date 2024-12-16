file = open("day15\day15.txt", 'r')
data = file.read()
mapRaw, movesRaw = data.split("\n\n")
walls, boxes = set(), set()
dirs = {"^":[-1,0], "v":[1,0], "<":[0,-1], ">":[0,1]}

#Getting location of all objects
for y, line in enumerate(mapRaw.split("\n")):
    for x, ch in enumerate(line):
        if(ch == "#"):
            walls.add((y, x))
        elif(ch == "O"):
            boxes.add((y, x))
        elif(ch == "@"):
            robot = [y, x]

#creating moves list
moves = []
for i in movesRaw.split("\n"):
    for ch in i:
        moves.append(ch)

#Function used for checking if boxes can be pushed, if no walls, boxes will be displaced
def push(box, dir):
    next = (box[0]+dir[0], box[1]+dir[1])
    if(next in walls):
        return False
    if(next in boxes):
        if(push(next, dir) == False): #check if when pushed, it ends with a wall
            return False
        
    boxes.remove((box))
    boxes.add(next)
    return True

#Going through all moves sets
for move in moves:
    next = (robot[0]+dirs[move][0], robot[1]+dirs[move][1])
    if(next in walls):
        continue
    if(next in boxes):
        if(push(next, dirs[move]) == False):
            continue
    robot = next

ans = 0
for box in boxes:
    ans += box[0]*100 + box[1]
print(ans)