import heapq
from collections import deque
file = file = open("day16\day16.txt", 'r')
start, end = (), () #record start and end pos
maze = []
dirs = ((-1,0), (0,-1), (1,0), (0,1)) #N, W, S, E. Arranged this way for more easier access
for y, i in enumerate(file):
    maze.append(list(i.strip())) #add layout into list
    for x, ch in enumerate(i):
        if(ch == "S"):
            start = (y, x)
        elif(ch == "E"):
            end = (y, x)


def dijkstra(): #algo that will move to every location and find its min cost relative to starting pt(Usually used for weighted graphs)
    state = (start[0], start[1], 3) #Data stored in state are the position and the direction. 3 as its index for East
    pq = [] #list used for priority queue
    heapq.heappush(pq, (0, state)) #list, (cost, data)
    visited = {state: 0} #dict to store all the min cost all pos needs
    while pq:
        cost, (y, x, d) = heapq.heappop(pq)
        if(visited.get((y,x,d), float('inf')) < cost): #continue if this state cost is not lower than recorded
            continue

        #Forward
        nextY, nextX = y+dirs[d][0], x+dirs[d][1]
        if(maze[nextY][nextX] != "#"): #check if next step is wall
            newCost = cost + 1
            if(newCost < visited.get((nextY, nextX, d), float('inf'))): #check if curr pos has been visited and if there is a better cost
                visited[(nextY, nextX, d)] = newCost
                heapq.heappush(pq, (newCost, (nextY, nextX, d)))

        #Turn CW and ACW
        for newD in [(d-1)%4, (d+1)%4]:
            if(maze[y][x] != "#"):
                newCost = cost + 1000 #turn only
                if(newCost < visited.get((y, x, newD), float('inf'))): #check if curr pos has been visited and if there is a better cost
                    visited[(y, x, newD)] = newCost
                    heapq.heappush(pq, (newCost, (y, x, newD)))

    return visited


def backtrack(part1):
    bestPath = set() #Used to store all pos along best path
    stack = deque() #Last in first out
    for i in range(4): #checking which direction has best cost
        if((end[0], end[1], i) in visited and visited[(end[0], end[1], i)] == part1):
            stack.append((end[0], end[1], i)) #adding the ending state from part1
    while(stack):
        y, x, d = stack.pop()
        cost = visited[(y, x, d)]

        #moving backwards
        backY, backX = y-dirs[d][0], x-dirs[d][1]
        if(maze[backY][backX] != "#"): #check if next step is wall
            prevCost = cost - 1
            if(prevCost >= 0):
                prevState = (backY, backX, d)
                if(prevState in visited and visited[prevState]==prevCost): #Check if it was this was the correct path taken in part 1
                    stack.append(prevState)
                    bestPath.add(prevState)
        
        #Turning cw and acw
        for newD in [(d-1)%4, (d+1)%4]:
            if(maze[y][x] != "#"): #check if next step is wall
                prevCost = cost - 1000
                if(prevCost >= 0):
                    prevState = (y, x, newD)
                    if(prevState in visited and visited[prevState]==prevCost): #Check if it was this was the correct path taken in part 1
                        stack.append(prevState)
                        bestPath.add(prevState)

    #Remove same x,y with different d from bestPath
    ans = set()
    for pos in bestPath:
        if((pos[0], pos[1]) not in ans):
            ans.add((pos[0], pos[1]))
    return ans


visited = dijkstra()
part1 = float('inf')
for i in range(4): #checking which direction has best cost
    if(visited.get((end[0], end[1], i), 0) != 0):
        part1 = min(visited[(end[0], end[1], i)], part1)
part2 = backtrack(part1)
print(part1)
print(len(part2)) 