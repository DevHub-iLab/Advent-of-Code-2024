import aocd
input = aocd.get_data(year=2024, day=8)
# input = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

uniqueChars = set(input)
uniqueChars.remove("\n")
uniqueChars.remove(".")

map = input.split("\n")
map = [list(row) for row in map]

rows = len(map)
cols = len(map[0])

charCoords = {}
antiPosList = []

for char in uniqueChars:
    coords = [(i, j) for i in range(len(map)) for j in range(len(map[i])) if map[i][j] == char]
    charCoords[char] = coords

def in_bounds(pos):
    return pos[0] >= 0 and pos[0] < rows and pos[1] >= 0 and pos[1] < cols

### Part 1

for char, coords in charCoords.items():
    # Pairwise difference, check if in bounds of map
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j:
                continue
            # From i to j
            diff = (coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
            if diff[0] == 0 and diff[1] == 0:
                continue
            # Check if diff is in bound
            if in_bounds((coords[i][0] + diff[0], coords[i][1] + diff[1])):
                antiPos = (coords[i][0] + diff[0], coords[i][1] + diff[1])

                if antiPos not in antiPosList:
                    antiPosList.append(antiPos)

print(len(antiPosList))


### Part 2. A simple modification to the above code
antiPosList2 = []

for char, coords in charCoords.items():
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j:
                continue
            # From j to i instead.
            diff = (coords[j][0] - coords[i][0], coords[j][1] - coords[i][1])
            origDiff = diff

            # All antinodes along directed half line
            while in_bounds((coords[i][0] + diff[0], coords[i][1] + diff[1])):
                antiPos = (coords[i][0] + diff[0], coords[i][1] + diff[1])
                # if antiPos not in all_nodes:
                if antiPos not in antiPosList2:
                    antiPosList2.append(antiPos)
                diff = (diff[0] + origDiff[0], diff[1] + origDiff[1])

print(len(antiPosList2))
