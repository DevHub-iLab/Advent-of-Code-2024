import math

file = open("txt\day6.txt", 'r')
map = []
playerX, playerY= 0, 0
yCnt = 0
distinct = 0

for i in file:
    line = list(i) #dont need to use split()
    try:
        playerX = line.index("^") #locate x coor of player
        playerY = yCnt #locate y coor of player
        line[playerX] = "X" #replace "^" with "X"
        distinct += 1
    except ValueError:
        yCnt += 1
    map.append(line)


x, y = 0, 1
dir = 0
while(playerX+x<len(map[0]) and playerX+x>=0 and playerY-y<len(map) and playerY-y>=0):
    x, y = int(math.sin(dir*(math.pi/180))), int(math.cos(dir*(math.pi/180))) #find which x and y direction to move
    if(map[playerY-y][playerX+x] == "#"):
        dir += 90
    else:
        if(map[playerY-y][playerX+x] == "."):
            playerX = playerX+x
            playerY = playerY-y
            map[playerY][playerX] = dir%360 #same thing as "X"
            distinct += 1
        else:
            playerX = playerX+x
            playerY = playerY-y

print("part 1:", distinct)

#Not gonna include part 2