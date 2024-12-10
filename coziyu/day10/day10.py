import aocd
input = aocd.get_data(year=2024, day=10)

# Turn input into 2d array of numbers
input = [[int(x) for x in line] for line in input.split("\n")]

### Part 1 - need number of distinct reachable 9s

def find_score(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dfs(r, c, reachable):
        if grid[r][c] == 9:
            reachable.add((r, c))
            return 1
        total = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c] + 1 and (nr, nc) not in reachable:
                total += dfs(nr, nc, reachable)
        return total

    total_score = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_score += dfs(r, c, set())
    
    return total_score

print(find_score(input)) 

### Part 2 - now we need number of distinct paths 
def find_rating(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c, path):
        if grid[r][c] == 9:
            return 1
        total = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c] + 1:
                total += dfs(nr, nc, path + [(nr, nc)])
        return total
    
    total_rating = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_rating += dfs(r, c, [(r, c)])
    return total_rating
    

print(find_rating(input)) 

