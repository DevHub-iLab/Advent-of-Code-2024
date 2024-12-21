import aocd
input = aocd.get_data(day=21, year=2024)

# input = """029A
# 980A
# 179A
# 456A
# 379A"""

input = input.split("\n")
input = [line.strip() for line in input]

# print(input)

### Part 1 - DP on all pair all paths

coords_num = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '0': (1, 3),
    'A': (2, 3)
}
coords_dir = {
    '^': (1, 0),
    'A': (2, 0), 
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1)
}

directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

from itertools import permutations
from functools import lru_cache
@lru_cache(None)
def legal_key_sequences(start, end, is_numeric):
    if is_numeric:
        forbidden = (0, 3)
    else:
        forbidden = (0, 0)
    dx, dy = end[0] - start[0], end[1] - start[1]
    keypresses = []

    if dx > 0:
        keypresses.extend(['>'] * abs(dx))
    else:
        keypresses.extend(['<'] * abs(dx))
    
    if dy > 0:
        keypresses.extend(['v'] * abs(dy))
    else:
        keypresses.extend(['^'] * abs(dy))

    legal_key_sequences = []
    for sequence in permutations(keypresses):
        visited = [start]
        legal = True
        for keypress in sequence:
            next = (visited[-1][0] + directions[keypress][0], visited[-1][1] + directions[keypress][1])
            # We will never go out of bounds
            # Just check for forbidden position
            if next == forbidden:
                # print("Forbidden position", start, end, sequence)
                legal = False
                break
            visited.append(next)
        if legal:
            legal_key_sequences.append("".join(sequence)+'A')
    
    # Empty path
    if len(legal_key_sequences) == 0:
        return ['A']
    return legal_key_sequences

@lru_cache(None)
def find_min_seq_length(sequence, max_depth, depth): # depth is how many robots deep we are
    is_numeric = depth == 0
    coords = coords_num if is_numeric else coords_dir
    curr = coords['A']

    total_len = 0
    for char in sequence:
        next = coords[char]
        legal_sequences = legal_key_sequences(curr, next, is_numeric)
        # print(legal_sequences)
        if depth == max_depth:
            # Shortest sequence works
            total_len += len(min(legal_sequences))
        else:
            total_len += min(find_min_seq_length(seq, max_depth, depth + 1) for seq in legal_sequences)
        curr = next

    return total_len

def complexity(code, seq_len):
    num = int(code[0:3])
    # print(seq_len, num)
    return num * seq_len

count = 0
for code in input:
    seq_len = find_min_seq_length(code, 2, 0)
    curr_complexity = complexity(code, seq_len)
    count += curr_complexity

print(count)

### Part 2 - Argument change
count2 = 0
for code in input:
    seq_len = find_min_seq_length(code, 25, 0)
    curr_complexity = complexity(code, seq_len)
    count2 += curr_complexity

print(count2)