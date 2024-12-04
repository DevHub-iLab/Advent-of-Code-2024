import aocd
input = aocd.get_data(year=2024, day=4)

### Part 1
# Classic multidirection search problem

grid = input.split("\n")
word = "XMAS"

def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (-1, 0),  # u
        (1, 0),   # d
        (0, -1),  # l
        (0, 1),   # r
        (-1, -1), # ul
        (-1, 1),  # ur
        (1, -1),  # dl
        (1, 1),   # dr
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Try matching at (r, c) along direction (dr, dc)
    def match_from(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True

    count = 0

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if match_from(r, c, dr, dc):
                    count += 1

    return count



# Count occurrences
count1 = count_word_occurrences(grid, word)
print(count1)


### Part 2
# We now know that the pattern must be a 3x3 grid.
# So, just exhaustively search for each pattern in the grid
pattern1 = """M.M
.A.
S.S"""

pattern2 = """M.S
.A.
M.S"""

pattern3 = """S.M
.A.
S.M"""

pattern4 = """S.S
.A.
M.M"""

patterns = [pattern1, pattern2, pattern3, pattern4]


def count_pattern_occurrences(grid, pattern):
    rows = len(grid)
    cols = len(grid[0])
    pattern_rows = len(pattern.split("\n"))
    pattern_cols = len(pattern.split("\n")[0])
    count = 0
    
    # March each pattern against the grid
    # . is a wildcard that matches any character
    def is_match(r, c, pattern):
        for i, row in enumerate(pattern.split("\n")):
            for j, char in enumerate(row):
                if char != "." and grid[r + i][c + j] != char:
                    return False
        return True

    for r in range(rows - pattern_rows + 1):
        for c in range(cols - pattern_cols + 1):
            if is_match(r, c, pattern):
                count += 1

    return count

pat_count = [count_pattern_occurrences(grid, pattern) for pattern in patterns]
# print(pat_count)

count2 = sum(pat_count)
print(count2)