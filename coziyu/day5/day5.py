import aocd
input = aocd.get_data(year=2024, day=5)

### Preprocess input

inputParts = input.split("\n\n")

rules = inputParts[0].split("\n")
order = {}

for rule in rules:
    key, value = rule.split("|")
    if key in order:
        order[key].append(value)
    else:
        order[key] = [value]

updates = inputParts[1].split("\n")
updates = [update.split(",") for update in updates]

# Create a comparison function based on the order.
# For each key, the entries of order[key] must come AFTER key in the list.
# comp(x,y) = -1, x must go before y
# comp(x,y) = 0 if there is no order
# comp(x,y) = 1, x must go after y

def comp(x, y):
    if x == y:
        return 0
    if x in order:
        if y in order[x]:
            return -1
    if y in order:
        if x in order[y]:
            return 1
    return 0

from functools import cmp_to_key

def is_correct(update):
    return update == sorted(update, key=cmp_to_key(comp))


### Part 1

correctMidEntries = [update[len(update) // 2] for update in updates if is_correct(update)]
sum1 = sum([int(x) for x in correctMidEntries])

print(sum1)

### Part 2

sortedIncorrectUpdates = [sorted(update, key=cmp_to_key(comp)) for update in updates if not is_correct(update)]
incorrectMiddleEntries = [(update[len(update) // 2]) for update in sortedIncorrectUpdates]
sum2 = sum([int(x) for x in incorrectMiddleEntries])
print(sum2)