import aocd
input = aocd.get_data(day=15, year=2024)

# input = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# input = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<"""

# input = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^"""

grid = input.split("\n\n")[0]
grid = [list(row) for row in grid.split("\n")]
moves = input.split("\n\n")[1].replace("\n", "") # '\n' is in the damn input
moves = list(moves)


### Part 1 - simple recursive push propagation
def move(grid, pos, dir):
    r, c = pos
    type = grid[r][c]
    # print(f"Moving {type} from {r}, {c} in direction {dir}")
    if type == "#":
        return False

    nr, nc = r, c
    if dir == "^":
        nr = r - 1
    if dir == "v":
        nr = r + 1
    if dir == "<":
        nc = c - 1
    if dir == ">":
        nc = c + 1

    if grid[nr][nc] == "#":
        return False
    if grid[nr][nc] == "O":
        # Attempt to move "O" in the direction too.
        if not move(grid, (nr, nc), dir):
            return False
    
    grid[r][c] = "."
    grid[nr][nc] = type
    return True

def calc_score(grid):
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                score += i * 100 + j
    return score

for dir in moves:
    for r, row in enumerate(grid):
        if "@" in row:
            pos = (r, row.index("@"))
            break

    move(grid, pos, dir)

print(calc_score(grid))

### Part 2 - we have to seperate the movement check and the actual movement logic

grid = input.split("\n\n")[0]
grid = [list(row) for row in grid.split("\n")]

def widen_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == "#":
                new_row.append("#")
                new_row.append("#")
            elif cell == "O":
                new_row.append("[")
                new_row.append("]")
            elif cell == ".":
                new_row.append(".")
                new_row.append(".")
            elif cell == "@":
                new_row.append("@")
                new_row.append(".")
        new_grid.append(new_row)
    return new_grid

def check_move(grid, pos, dir):
    r, c = pos
    type = grid[r][c]
    if type == "#":
        return False
    if type == ".":
        return True

    nr, nc = r, c
    if dir == "^":
        nr = r - 1
    if dir == "v":
        nr = r + 1
    if dir == "<":
        nc = c - 1
    if dir == ">":
        nc = c + 1

    if dir == "^" or dir == "v":
        if grid[nr][nc] == "[":
            return check_move(grid, (nr, nc), dir) and check_move(grid, (nr, nc + 1), dir)
        if grid[nr][nc] == "]":
            return check_move(grid, (nr, nc), dir) and check_move(grid, (nr, nc - 1), dir)
        
    return check_move(grid, (nr, nc), dir)

def force_move(grid, pos, dir):
    r, c = pos
    type = grid[r][c]
    if type == "#":
        return False
    
    # print(f"Moving {type} from {r}, {c} in direction {dir}")

    nr, nc = r, c
    if dir == "^":
        nr = r - 1
    if dir == "v":
        nr = r + 1
    if dir == "<":
        nc = c - 1
    if dir == ">":
        nc = c + 1
    
    new_type = grid[nr][nc]
    if new_type == "#":
        return False
    
    if new_type == "[":
        if dir == "^" or dir == "v":
            force_move(grid, (nr, nc), dir)
            force_move(grid, (nr, nc + 1), dir)
            grid[r][c] = "."
            grid[nr][nc] = type
            return True
        else:
            force_move(grid, (nr, nc), dir)
            grid[r][c] = "."
            grid[nr][nc] = type
            return True
    
    if new_type == "]":
        if dir == "^" or dir == "v":
            force_move(grid, (nr, nc), dir)
            force_move(grid, (nr, nc - 1), dir)
            grid[r][c] = "."
            grid[nr][nc] = type
            return True
        else:
            force_move(grid, (nr, nc), dir)
            grid[r][c] = "."
            grid[nr][nc] = type
            return True
    
    grid[r][c] = "."
    grid[nr][nc] = type
    return True


def move2(grid, pos, dir):
    proceed = check_move(grid, pos, dir)
    if not proceed:
        return False
    force_move(grid, pos, dir)

def calc_score2(grid):
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                score += i * 100 + j
    return score

grid = widen_grid(grid)
for dir in moves:
    for r, row in enumerate(grid):
        if "@" in row:
            pos = (r, row.index("@"))
            break

    move2(grid, pos, dir)

print(calc_score2(grid))