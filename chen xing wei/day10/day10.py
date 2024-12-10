from collections import deque
topology = []
trailHeads = []
ans1, ans2 = 0, 0

with open("day10\day10.txt") as f:
    for line in f:
        line = list(map(int, list(line.strip())))
        for i in range(len(line)):
            if line[i] == 0:
                trailHeads.append((i, len(topology)))
        topology.append(line)

#####################(1) using stack or list########################
# for head in trailHeads:
#     reached = []
#     stack = deque()
#     stack.append(head)
#     while(len(stack) != 0):
#         currPos = stack.pop()
#         x, y = currPos[0], currPos[1]
#         currHeight = topology[y][x]
#         if(currHeight == 9):
#             if(currPos not in reached):
#                 reached.append(currPos)
#             ans2 += 1
#             continue

#         if(x-1>=0 and topology[y][x-1]==currHeight+1): #if can move left
#             stack.append((x-1, y))
#         if(x+1<len(topology[0]) and topology[y][x+1]==currHeight+1): #move right
#             stack.append((x+1, y))
#         if(y-1>=0 and topology[y-1][x]==currHeight+1): #move up
#             stack.append((x, y-1))
#         if(y+1<len(topology) and topology[y+1][x]==currHeight+1): #down
#             stack.append((x, y+1))
#     ans1 += len(reached)
###################################################################


##########################(2) using DFS############################
def dfs(x, y, prevHeight):
    # bounds
    if(x < 0 or y < 0 or x >= len(topology[0]) or y >= len(topology)):
        return
    
    # trail check
    if(topology[y][x]-prevHeight != 1): 
        return
    
    if(topology[y][x] == 9):
        global ans1, ans2
        if((x, y) not in visited):
            ans1 += 1
        ans2 += 1
        visited.add((x, y))
        return
    
    dfs(x+1, y, prevHeight+1)
    dfs(x-1, y, prevHeight+1)
    dfs(x, y+1, prevHeight+1)
    dfs(x, y-1, prevHeight+1)

for heads in trailHeads:
    visited = set()
    dfs(heads[0], heads[1], -1)
#####################################################################

print("Part 1:", ans1, "Part 1:", ans2)