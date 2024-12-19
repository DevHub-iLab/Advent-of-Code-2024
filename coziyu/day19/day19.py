import aocd
input = aocd.get_data(day=19, year=2024)

# input = """r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb"""

def parse(input):
    patterns, towels = input.split("\n\n")
    patterns = patterns.split(", ")
    towels = towels.split("\n")
    return tuple(patterns), towels

### Part 1 - Simple DP

from functools import lru_cache
@lru_cache(None)
def is_possible(towel, patterns):
    
    if len(towel) == 0:
        return True
    
    for pattern in patterns:
        if towel.startswith(pattern):
            if is_possible(towel[len(pattern):], patterns):
                return True

    return False

def count_possible_towels(input):
    patterns, towels = parse(input)

    return sum(is_possible(towel, patterns) for towel in towels)

print(count_possible_towels(input))

### Part 2 - Modification of DP in Part 1.
@lru_cache(None)
def num_possible(towel, patterns):
    
    if len(towel) == 0:
        return 1
    total = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            total += num_possible(towel[len(pattern):], patterns)
    
    return total

def count_possible_ways(input):
    patterns, towels = parse(input)

    return sum(num_possible(towel, patterns) for towel in towels)

print(count_possible_ways(input))