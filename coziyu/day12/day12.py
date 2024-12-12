import aocd
input = aocd.get_data(year=2024, day=12)

# input = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

input = [list(line) for line in input.split("\n")]

### Part 1 - Flood fill to find area and perimeter of each region.

def get_type(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return "~"
    return grid[r][c]

def find_region(grid, chr, r, c, visited):
    area = 1
    perimeter = 0

    visited.add((r, c))

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if get_type(grid, nr, nc) == chr:
            if (nr, nc) not in visited:
                del_area, del_perimeter = find_region(grid, chr, nr, nc, visited)
                area += del_area
                perimeter += del_perimeter
        else:
            perimeter += 1

    return area, perimeter

def find_price(grid):
    visited = set()
    price = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited:
                area, perimeter = find_region(grid, grid[r][c], r, c, visited)
                price += area * perimeter
    return price

price = find_price(input)
print(price)

### Part 2 - Key idea: every side touches 2 corners, and every corner touches 2 sides.
# Thus, the number of sides = number of corners
def find_region2(grid, chr, r, c, visited):
    area = 1
    corners = 0

    visited.add((r, c))

    chrU = get_type(grid, r - 1, c)
    chrD = get_type(grid, r + 1, c)
    chrL = get_type(grid, r, c - 1)
    chrR = get_type(grid, r, c + 1)
    chrUL = get_type(grid, r - 1, c - 1)
    chrUR = get_type(grid, r - 1, c + 1)
    chrDL = get_type(grid, r + 1, c - 1)
    chrDR = get_type(grid, r + 1, c + 1)

    # 90 degree corners
    if chrU != chr and chrL != chr:
        corners += 1
    if chrU != chr and chrR != chr:
        corners += 1
    if chrD != chr and chrL != chr:
        corners += 1
    if chrD != chr and chrR != chr:
        corners += 1

    # 270 degree corners
    if chrU == chr and chrL == chr and chrUL != chr:
        corners += 1
    if chrU == chr and chrR == chr and chrUR != chr:
        corners += 1
    if chrD == chr and chrL == chr and chrDL != chr:
        corners += 1
    if chrD == chr and chrR == chr and chrDR != chr:
        corners += 1

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if get_type(grid, nr, nc) == chr:
            if (nr, nc) not in visited:
                del_area, del_corner = find_region2(grid, chr, nr, nc, visited)
                area += del_area
                corners += del_corner

    return area, corners

def find_price2(grid):
    visited = set()
    price = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited:
                area, corners = find_region2(grid, grid[r][c], r, c, visited)
                # print(get_type(grid, r, c), area, corners)
                price += area * corners
    return price

price = find_price2(input)
print(price)
