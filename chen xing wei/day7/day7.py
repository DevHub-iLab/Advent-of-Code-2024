file = open("day7\day7.txt", 'r')
eqn = {}
ans = 0
for line in file:
    key, string = line.split(": ")
    value = string.strip().split(" ")
    eqn[key] = value

for key in eqn.keys():
    mem = [int(eqn[key][0])]
    for i in range(1, len(eqn[key])):
        newMem = []
        for j in range(len(mem)):
            newMem.append(mem[j] * int(eqn[key][i]))
            newMem.append(mem[j] + int(eqn[key][i]))
            newMem.append(int(str(mem[j]) + str(eqn[key][i]))) #Uncomment for part 2
        mem = newMem
    if(int(key) in mem):
        ans += int(key)
print(ans)