import aocd
input = aocd.get_data(day=25, year=2024)


# input = """#####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####

# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####"""

### Part 1
def parse(input):
    locks_and_keys = input.split("\n\n")
    locks = [] # top row is full of #
    keys = []  # bot row is full of #

    for item in locks_and_keys:
        if item[0:5] == "#####":
            locks.append([list(row) for row in item.split("\n")])  
        else:
            keys.append([list(row) for row in item.split("\n")])
    return locks, keys

def to_height(item):
    out = []
    for i in range(len(item[0])):
        sum = 0
        for j in range(len(item)):
            if item[j][i] == "#":
                sum += 1
        out.append(sum)
    return out
locks, keys = parse(input)
# print(to_height(locks))

locks = [to_height(lock) for lock in locks]
keys = [to_height(key) for key in keys]
# print(locks)
# print(keys)

def is_match(lock, key):
    return all([lock[i] + key[i] <= 7 for i in range(len(lock))])

def find_match(lock_heights, key_heights):
    matches = []
    for i in range(len(lock_heights)):
        for j in range(len(key_heights)):
            if is_match(lock_heights[i], key_heights[j]):
                matches.append((i, j))
    return matches

matches = find_match(locks, keys)
print(len(matches))
# print(matches)

# Part 2 - Merry Christmas!