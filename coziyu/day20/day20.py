import aocd
input = aocd.get_data(day=20, year=2024)

# input = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""

def parse(input):
    grid = input.split("\n")
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                start = (x, y)
            if grid[y][x] == "E":
                end = (x, y)
    return grid, start, end

### Part 1 - Simple brute force on the paths

def bfs(grid, start, end):
    visited = set()
    visited.add(start)
    queue = [(start, None, 0)]
    while queue:
        state = queue.pop(0)
        pos, prev, dist = state
        x, y = pos
        if (x, y) == end:
            path = [end]
            _prev = prev
            while _prev:
                _pos, _prev, _dist = _prev
                path.append(_pos)
            return dist, path[::-1]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#" and (nx, ny) not in visited:
                queue.append(((nx, ny), state, dist + 1))
                visited.add((nx, ny))
    return -1

def count_cheats(path):
    out = 0
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            dist = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
            saved = j - (i + dist)
            if dist == 2 and saved >= 100:
                out += 1
    return out

dist, path = bfs(*parse(input))
print(count_cheats(path))

# Part 2 - Modify search conditions
def count_cheats2(path):
    out = 0
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            dist = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
            saved = j - (i + dist)
            if dist <= 20 and saved >= 100:
                out += 1
    return out

print(count_cheats2(path))