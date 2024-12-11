file = open("day7\day7.txt", 'r')
eqn = {}
ans = 0
for line in file:
    key, string = line.split(": ")
    value = string.strip().split(" ")
    eqn[key] = value

# print(eqn)
# for key in eqn.keys():
#     mem = [int(eqn[key][0])]
#     for i in range(1, len(eqn[key])):
#         newMem = []
#         for j in range(len(mem)):
#             newMem.append(mem[j] * int(eqn[key][i]))
#             newMem.append(mem[j] + int(eqn[key][i]))
#             newMem.append(int(str(mem[j]) + str(eqn[key][i]))) #Uncomment for part 2
#         mem = newMem #mem will only record numbers that has been through the most # of operations
#     if(int(key) in mem):
#         ans += int(key)
# print(ans)


def recursive_operator(value, position, key):
    if position>=len(array):
        return value==key
    if recursive_operator(value*array[position],position+1, key):
        return True
    if recursive_operator(value+array[position],position+1, key):
        return True
    if recursive_operator(int(str(value) + str(array[position])), position+1, key):
        return True
    return False
for key in eqn.keys():
    array = list(map(int, eqn[key]))
    if(recursive_operator(array[0], 1, int(key))):
        ans += int(key)
print(ans)