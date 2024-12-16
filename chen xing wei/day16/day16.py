import heapq
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


def dijktra(): #algo that will move to every location and find its min cost relative to starting pt(Usually used on weighted graphs)
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

        #CW and ACW forward
        for newD in [(d-1)%4, (d+1)%4]:
            nextY, nextX = y+dirs[newD][0], x+dirs[newD][1]
            if(maze[nextY][nextX] != "#"):
                newCost = cost + 1001 #turn and move
                if(newCost < visited.get((nextY, nextX, newD), float('inf'))): #check if curr pos has been visited and if there is a better cost
                    visited[(nextY, nextX, newD)] = newCost
                    heapq.heappush(pq, (newCost, (nextY, nextX, newD)))

    return visited


visited = dijktra()
ans = float('inf')
for i in range(4): #checking which direction has best cost
    if((end[0], end[1], i) in visited):
        ans = min(visited[(end[0], end[1], i)], ans)
print(ans) #Part 1