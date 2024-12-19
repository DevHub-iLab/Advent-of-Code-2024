file = open("day18\day18.txt", "r")
BYTES = []
walls = set()
low, high = 0, 0
for size, i in enumerate(file):
    x, y = i.strip().split(',')
    BYTES.append((int(x), int(y)))
    high = size+1
for i in range(1024): #For part 1
    walls.add(BYTES[i])

def bfs():
    visited = []
    queue = []
    path = {} #Used to record the min cost for each pos
    visited.append((0,0))
    queue.append(((0,0), 0))

    while(queue):
        pos, cost = queue.pop(0) #FIFO
        path[pos] = cost #Updating cost
        for dir in [[-1,0], [1,0], [0,-1], [0,1]]: #Iterating all directions
            next = (pos[0]+dir[0], pos[1]+dir[1]) 
            if(next[0]<0 or next[0]>70 or next[1]<0 or next[1]>70 or next in walls): #Checking validity
                continue
            if(next not in visited): #Only considering first visits, as any other visits will be more ex
                visited.append(next)
                queue.append((next, cost+1))
    return path.get((70,70), 0) #return cost it can reach ending, else 0

print("Part 1:", bfs())
while(low < high): #Binary search
    mid = (low+high) // 2 + 1
    walls = set() #Clear walls
    for i in range(mid):
        walls.add(BYTES[i])
    if(bfs() == 0):
        high = mid - 1
    else:
        low = mid
    print(low , high)
print("Part 2:", BYTES[mid])