file = open("day4\day4.txt", "r")
puzzle = []
for line in file:
    puzzle.append(list(line.strip()))

#Part 1
ans1 = 0
dirs = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]] #eight principal wind
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        #if "X" is found check if it will be in range by finding if it can move 3 steps
        if(puzzle[i][j] == "X"):
            for dir in dirs: #looping all 8 winds
                if(i+dir[0]*3<len(puzzle) and i+dir[0]*3>=0 and j+dir[1]*3<len(puzzle[0]) and j+dir[1]*3>=0): #checking range
                    if("MAS" == puzzle[i+dir[0]][j+dir[1]] + puzzle[i+dir[0]*2][j+dir[1]*2] + puzzle[i+dir[0]*3][j+dir[1]*3]):
                        ans1 += 1

#Part 2
ans2 = 0
cross = [[1,1], [1,-1], [-1,-1], [-1,1]]
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        if(puzzle[i][j] == "A"): #if "A" is found we check if the 4 corners are out of range, else check if it forms "MAS"
            if(i>0 and j>0 and i<len(puzzle)-1 and j<len(puzzle[0])-1): #checking range
                line1 = puzzle[i+cross[0][0]][j+cross[0][1]] + puzzle[i+cross[2][0]][j+cross[2][1]]
                line2 = puzzle[i+cross[1][0]][j+cross[1][1]] + puzzle[i+cross[3][0]][j+cross[3][1]]
                if((line1=="MS" or line1=="SM") and (line2=="MS" or line2=="SM")):
                    ans2 += 1
print("1:", ans1, "\n2:", ans2)