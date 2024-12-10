import itertools

f = open("/workspaces/Advent-of-Code-2024/emily7lim/day7/data.txt", "r")
contents = f.read().split("\n")
sum = 0
for i in contents:
    ans = i.split(": ")[0]
    eqn = i.split(": ")[1].split(" ")
    numbers=len(eqn)-1
    for i in itertools.product("*+", repeat=numbers):
        eqnans = int(eqn[0])
        for j in range(len(i)):
            if i[j] == "*":
                eqnans *= int(eqn[j+1])
            elif i[j] == "+":
                eqnans += int(eqn[j+1])
        if eqnans == int(ans):
            sum += eqnans
            break

print(sum)