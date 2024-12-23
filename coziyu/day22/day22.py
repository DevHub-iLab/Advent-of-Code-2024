import aocd
input = aocd.get_data(day=22, year=2024)

# input = """1
# 10
# 100
# 2024"""

# input = """1
# 2
# 3
# 2024"""

### Part 1 - Implementing the PRNG
def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def next(n):
    n = prune(mix(n * 64, n))
    n = prune(mix(n // 32, n))
    n = prune(mix(n * 2048, n))
    return n

def nextk(n, k):
    for _ in range(k):
        n = next(n)
    return n

def parse(input):
    return [int(x) for x in input.split("\n")]

initial_vals = parse(input)
print(sum([nextk(x, 2000) for x in initial_vals]))

### Part 2 - Iteratively calculating profits. Nothing special
def nextk_10(n, k):
    arr = [n % 10]
    for _ in range(k):
        n = next(n)
        arr.append(n % 10)
    return arr

from collections import Counter
def max_profit(initial_vals):
	monkey_prices = []
	monkey_diffs = []
	for x in initial_vals:
		price_list = nextk_10(x, 2000)
		price_diffs = [price_list[i + 1] - price_list[i] for i in range(len(price_list) - 1)]

		monkey_prices.append(price_list)
		monkey_diffs.append(price_diffs)
        
	profits = Counter()
	for monkey_ind, price_diff_seq in enumerate(monkey_diffs):
		found = set() # we only want the 1st instance of every 4-tuple
		for j in range(3, len(price_diff_seq)):
			seq = tuple(price_diff_seq[j - 3:j + 1])
			if seq not in found:
				profits[seq] += monkey_prices[monkey_ind][j + 1]
				found.add(seq)
	return max(profits.values())

print(max_profit(initial_vals))

