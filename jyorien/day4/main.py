graph = []
with open("input.txt") as file:
    for line in file:
        line = list(line.strip())
        graph.append(line)

############## PART 1 ##############
rows = len(graph)
cols = len(graph[0])
count = 0
dirs = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1),(1,-1), (-1,-1))
def dfs(graph, x, y, word, dx, dy):
    if len(word) == 0:
        global count
        count += 1
        return
    
    global rows
    global cols
    nextWord = word[0]
    new_x = x+dx
    new_y = y+dy
    if new_x >= 0 and new_x < cols and new_y >= 0 and new_y < rows and graph[new_y][new_x] == nextWord:
        dfs(graph, new_x, new_y, word[1:], dx, dy)
    
for i in range(rows):
    for j in range(cols):
        if graph[i][j] == 'X':
            for dx, dy in dirs:
       
                dfs(graph, j, i, "MAS", dx,dy)

print(count)
############## PART 1 ##############

############## PART 2 ##############
rows = len(graph)
cols = len(graph[0])
count = 0

def diagonalDFS(graph, x, y, word, dx, dy):
    if len(word) == 0:
        return True
    nextWord = word[0]
    global rows
    global cols
    new_x = x+dx
    new_y = y+dy
    if new_x >= 0 and new_x < cols and new_y >= 0 and new_y < rows and graph[new_y][new_x] == nextWord:
        return diagonalDFS(graph, new_x, new_y, word[1:], dx, dy)
    return False
    



dirs = ((-1,-1), (-1,1)) # diagonals only
for i in range(rows):
    for j in range(cols):
        if graph[i][j] == 'A':
            isValid1 = False
            isValid2 = False
            if i-1 >= 0 and i-1 < rows and j-1 >= 0 and j-1 < cols:
                if graph[i-1][j-1] == 'M':
                    isValid1 = diagonalDFS(graph, j-1, i-1, "AS", 1,1)
                elif graph[i-1][j-1] == 'S':
                    isValid1 = diagonalDFS(graph, j-1, i-1, "AM", 1,1)

            if i-1 >= 0 and i < rows and j+1 >= 0 and j+1 < cols:
                if graph[i-1][j+1] == 'M':
                    isValid2 = diagonalDFS(graph, j+1, i-1, "AS", -1,1)
                elif graph[i-1][j+1] == 'S':
                    isValid2 = diagonalDFS(graph, j+1, i-1, "AM", -1,1)
            if isValid1 and isValid2:
                count += 1

print(count)


############## PART 2 ##############

