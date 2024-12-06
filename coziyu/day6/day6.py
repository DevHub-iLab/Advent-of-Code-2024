import aocd
input = aocd.get_data(year=2024, day=6)

grid = input.split("\n")
grid = [list(row) for row in grid]

### Part 1. Simple traversal

def count_unique_paths(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dirmap = {'^': 0, '>': 1, 'v': 2, '<': 3}

    if grid[r][c] in dirmap:
        guardPos = (r, c)
        facing = dirmap[grid[r][c]]
    else:
        print("Guard not found")
        return

    visited = set()
    visited.add((guardPos, facing))

    while True:
        dr, dc = dirs[facing]
        frontPos = (guardPos[0] + dr, guardPos[1] + dc)
        
        # Check for bounds
        if not (0 <= frontPos[0] < rows and 0 <= frontPos[1] < cols):
            break

        # Check for # in front
        if grid[frontPos[0]][frontPos[1]] == '#':
            facing = (facing + 1) % 4
        else:
            guardPos = frontPos
            visited.add((guardPos, facing))

    # Return unique postions only
    markedPos = set()
    for pos, _ in visited:
        markedPos.add(pos)
    return len(markedPos), markedPos

startPos = None

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] in "^>vV<":
            startPos = (r, c)
            break

count1,markedPos = count_unique_paths(grid, startPos[0], startPos[1])
print(count1)

### Part 2. 
# Try adding a # to each position and check if a loop occurs.

def is_loop(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dirmap = {'^': 0, '>': 1, 'v': 2, '<': 3}

    if grid[r][c] in dirmap:
        guardPos = (r, c)
        facing = dirmap[grid[r][c]]
    else:
        print("Guard not found")
        return

    visited = set()
    visited.add((guardPos, facing))

    while True:
        dr, dc = dirs[facing]
        frontPos = (guardPos[0] + dr, guardPos[1] + dc)

        # Check for bounds
        if not (0 <= frontPos[0] < rows and 0 <= frontPos[1] < cols):
            return False

        # Check for # in front
        if grid[frontPos[0]][frontPos[1]] == '#':
            facing = (facing + 1) % 4
        else:
            # Same state reached, loop acquired
            if (frontPos, facing) in visited:
                return True
            guardPos = frontPos
            visited.add((guardPos, facing))

count2 = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        # No need to place # on positions guards never visited 
        if (r,c) in markedPos:
            if grid[r][c] == '.':
                grid[r][c] = '#'
                if is_loop(grid, startPos[0], startPos[1]):
                    # print(f"Loop @ ({r}, {c})")
                    count2 += 1
                grid[r][c] = '.'

print(count2)
