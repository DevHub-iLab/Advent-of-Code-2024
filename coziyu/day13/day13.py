import aocd
input = aocd.get_data(year=2024, day=13)

# input = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""

### Custom Test Case for parallel
# input = """Button A: X+200, Y+100
# Button B: X+300, Y+150
# Prize: X=3400, Y=1700"""


import re

def parse(game_str):
    button_a = re.search(r"Button A: X(\+\d+), Y(\+\d+)", game_str)
    button_b = re.search(r"Button B: X(\+\d+), Y(\+\d+)", game_str)
    prize = re.search(r"Prize: X=(\d+), Y=(\d+)", game_str)

    a_x = int(button_a.group(1))
    a_y = int(button_a.group(2))
    b_x = int(button_b.group(1))
    b_y = int(button_b.group(2))
    p_x = int(prize.group(1))
    p_y = int(prize.group(2))


    return [(a_x, a_y), (b_x, b_y), (p_x, p_y)]

games = [parse(game) for game in input.split("\n\n")]


### Part 1 - Just brute force will do.

def calc_tokens(game):
    a_x, a_y = game[0]
    b_x, b_y = game[1]
    p_x, p_y = game[2]

    min_tokens = 0
    found = False
    for a in range(101):
        for b in range(101):
            if a * a_x + b * b_x == p_x and a * a_y + b * b_y == p_y:
                tokens = 3 * a + b
                if found == False:
                    min_tokens = tokens
                    found = True
                if tokens < min_tokens:
                    min_tokens = tokens

    return min_tokens
        
sum = 0
for game in games:
    sum += calc_tokens(game)
print(sum)


### Part 2 - should have seen it coming, never do brute force for part 1. 
# We are just solving a system of of 2 linear diophantine equations.
# There should be a fast algorithm possible by abusing Cramer's rule, but 
# I can't think of one quickly so I'll just use interger linear programming instead. 

def parse2(game_str):
    a,b,p = parse(game_str)
    p_x, p_y = p
    p = (10000000000000 + p_x,10000000000000 + p_y)

    return [a,b,p]

games = [parse2(game) for game in input.split("\n\n")]

import z3
def solve_ilp(a_del, b_del, prize):
    a_x, a_y = a_del
    b_x, b_y = b_del
    p_x, p_y = prize

    sys = z3.Optimize()
    a, b = z3.Ints('A B')
    
    sys.add(a >= 0)
    sys.add(b >= 0)
    sys.add(a_x * a + b_x * b == p_x)
    sys.add(a_y * a + b_y * b == p_y)
    sys.minimize(a * 3 + b)

    if sys.check() == z3.sat:
        model = sys.model()
        return model.eval(3 * a + b).as_long()

    return 0

def calc_tokens2(game):
    return solve_ilp(*game)

sum = 0
for game in games:
    sum += calc_tokens2(game)
print(sum)


### Part 2 - Better solution by solving the system of equations directly. We can use Cramer's rule.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve_cramer(game):
    a_x, a_y = game[0]
    b_x, b_y = game[1]
    p_x, p_y = game[2]

    det = a_x * b_y - a_y * b_x
    det_a = p_x * b_y - p_y * b_x
    det_b = a_x * p_y - a_y * p_x

    if det == 0:
        # Check if solutions exist
        gcd_x = gcd(a_x, b_x)
        if p_x % gcd_x != 0:
            return 0
        
        gcd_y = gcd(a_y, b_y)
        if p_y % gcd_y != 0:
            return 0
        
        # Press B first.
        n_x, r_x = divmod(p_x, b_x)
        n_y, r_y = divmod(p_y, b_y)

        n = min(n_x, n_y)

        while (p_x - n * b_x) % a_x != 0 or (p_y - n * b_y) % a_y != 0:
            n -= 1
        
        m = (p_x - n * b_x) // a_x
        
        return 3 * m + n

    # Cramer's rule
    a, da = divmod(det_a, det)
    b, db = divmod(det_b, det)

    if da == 0 and db == 0 and a >= 0 and b >= 0:
        return 3 * a + b
    return 0

sum = 0
for game in games:
    sum += solve_cramer(game)
print(sum)