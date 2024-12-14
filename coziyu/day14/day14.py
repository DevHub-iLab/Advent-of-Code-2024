import aocd

input = aocd.get_data(day=14, year=2024)

rows = 103
cols = 101

# input = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""

# rows = 7
# cols = 11

import re
def parse(line):
    pattern = r"p=(-?\d+,-?\d+) v=(-?\d+,-?\d+)"
    matches = re.match(pattern, line)
    matches = matches.groups()
    p = matches[0].split(",")
    v = matches[1].split(",")
    return [(int(p[0]), int(p[1])), (int(v[0]), int(v[1]))]

robots = [parse(line) for line in input.split("\n")]
# print(robots)

def move(robot, steps):
    pos = robot[0]
    vel = robot[1]
    pos = (pos[0] + steps * vel[0], pos[1] + steps * vel[1])
    pos = (pos[0] % cols, pos[1] % rows)
    return pos

def move_all(robots, steps):
    return [move(robot, steps) for robot in robots]

def count_robots_in_quadrants(robot_pos):
    # Robots that are exactly in the middle (horizontally or vertically) don't count as being in any quadrant
    quadrants = [0, 0, 0, 0]
    for pos in robot_pos:
        x = pos[0]
        y = pos[1]
        if x < cols // 2 and y < rows // 2:
            quadrants[0] += 1
        elif x > cols // 2 and y < rows // 2:
            quadrants[1] += 1
        elif x < cols // 2 and y > rows // 2:
            quadrants[2] += 1
        elif x > cols // 2 and y > rows // 2:
            quadrants[3] += 1

    return quadrants

quardrants = count_robots_in_quadrants(move_all(robots, 100))
product = 1
for factor in quardrants:
    product *= factor
print(product)


def find_largest_connected_region(robots_pos):
    visited = set()
    largest_connected_region = 0
    for pos in robots_pos:
        if pos in visited:
            continue
        region_size = 0
        stack = [pos]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            region_size += 1
            x = current[0]
            y = current[1]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dx == 0 and dy == 0:
                    continue
                new_x = x + dx
                new_y = y + dy
                if (new_x, new_y) in robots_pos:
                    stack.append((new_x, new_y))
        largest_connected_region = max(largest_connected_region, region_size)
    return largest_connected_region


def print_grid(robots_pos):
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    for pos in robots_pos:
        grid[pos[1]][pos[0]] = "#"
    for row in grid:
        print("".join(row))

import builtins
builtins.input("Press any key for part 2...")

max_size = 0
for i in range(1,100000): # Use another hueuristic if this doesn't work
    pos = move_all(robots, i)
    size = find_largest_connected_region(move_all(robots, i))
    if size >= max_size:
        max_size = size
        print_grid(pos)
        print(i, size)
