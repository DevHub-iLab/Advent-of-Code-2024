import aocd
input = aocd.get_data(day=18, year=2024)
# input = """5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0"""

from collections import deque

def parse(input):
    coordinates = []
    for line in input.strip().split("\n"):
        x, y = map(int, line.split(","))
        coordinates.append((x, y))
    return coordinates

def add_walls(grid_size, coordinates, max_bytes):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for i, (x, y) in enumerate(coordinates):
        if i >= max_bytes:
            break
        grid[y][x] = 1 
    # for row in grid:
    #     print("".join([str(i) for i in row]))
    return grid

def bfs(grid, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, 0, [start])])  # (pos, steps, path)
    visited = set([start])

    while queue:
        (x, y), steps, path = queue.popleft()

        if (x, y) == end:
            return steps, path + [(x, y)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] == 0:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1, path + [(nx, ny)]))

    return -1, []  # No path found    

def print_grid(grid, path):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) in path:
                print("o", end="")
            elif cell == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()

### Part 1
size = 71
start = (0, 0)
end = (size - 1, size - 1)

coordinates = parse(input)
grid = add_walls(size, coordinates, 1024)
length, path = bfs(grid, start, end)
print(length)

### Part 2
# Alternatively, use binary search 
for i, coord in enumerate(coordinates):
    grid2 = add_walls(size, coordinates, i + 1)
    length2, path2 = bfs(grid2, start, end)
    # print(i + 1, coord)
    # print_grid(grid2, path2)
    if length2 == -1:
        print(f"{coord[0]},{coord[1]}")
        break


