import aocd
input = aocd.get_data(year=2024, day=11)
# input = """125 17"""

# Turn input into list of numbers
input = list(map(int, input.split(" ")))

### Part 1 - Simple iteration
def apply_rules(stone):
    str_stone = str(stone)
    # Rule 1
    if stone == 0:
        return [1]

    # Rule 2
    if len(str_stone) % 2 == 0:
        mid = len(str_stone) // 2
        left_part = int(str_stone[:mid])
        right_part = int(str_stone[mid:])
        return [left_part, right_part]

    # Rule 3
    return [stone * 2024]

def apply_rules_array(stones):
    newStones = []
    for stone in stones:
        newStones.extend(apply_rules(stone))
    return newStones


def blink(initial_stones, blinks):
    stones = initial_stones
    for i in range(blinks):
        stones = apply_rules_array(stones)
        # print(f"{i + 1}: {len(stones)}")
    return len(stones)


blinks = 25
count1 = blink(input, blinks)
print(count1)

### Part 2 - remove redundant calls to apply_rules by using the right data structure - a multiset
# Main Observations:
# We don't need to preserve the order of stones - they can be processed in any order
# The stones present in the next iteration can be determined just by the stones
# in the current iteration, without relying on their order
#
# Suppose apply_rules(A) = B, and we have X stones that are equal to A in this iteration,
# Instead of calling apply_rules(A) X times, do it once, and add B to the next iteration X times  
#
# Thus, the correct data structure to store the stones is a multiset, rather than a list

def blink_memo(initial_stones, blinks):
    # Use queue to track stones count
    queue = [(stone, 1) for stone in initial_stones]
    
    for i in range(blinks):
        next = {}

        while queue:
            stone, multiplicity = queue.pop(0)

            # Applying memoization to apply_rules doesn't help much.
            # The reduction in the average case time complexity dominates 
            # the time reduction compared to memoization on apply_rules  
            results = apply_rules(stone)

            for new_stone in results:
                if new_stone not in next:
                    next[new_stone] = 0
                next[new_stone] += multiplicity

        for stone, multiplicity in next.items():
            queue.append((stone, multiplicity))

        # print(f"{i + 1}: {sum(next.values())}")

    return sum(count for _, count in queue)



blinks = 75

count2 = blink_memo(input, blinks)
print(count2)

# The worst case time complexity is still exponential I believe.
# However, the number of calls to apply_rules is reduced significantly