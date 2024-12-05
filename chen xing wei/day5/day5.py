file = open("day5.txt", 'r')
data = file.read()
inputParts = data.split("\n\n") #split rules and updates
rules = inputParts[0].split("\n")
order = {}

#create dict with the rules for each key
for rule in rules:
    key, value = rule.split("|")
    if key in order:
        order[key].append(value)
    else:
        order[key] = [value]

#Part 1
ans1 = 0
updates = inputParts[1].split("\n")
for i in updates:
    update = i.split(",")
    flag = True #used to check if line is correct
    for j in range(len(update)):
        for k in range(j+1, len(update)):
            if(update[k] not in order[update[j]]): #check if rules are followed
                flag = False
                break
        if(not flag):
           break
    if(flag): #if line is correct sum it
        ans1 += int(update[len(update)//2])
print(ans1)


#Part 2
ans2 = 0
updates = inputParts[1].split("\n")
for i in updates:
    update = i.split(",")
    flag = True #used to check if the current line is incorrect
    j = 0
    while j < len(update):
        for k in range(j+1, len(update)):
            if(update[k] not in order[update[j]]):
                update[k], update[j] = update[j], update[k] #swapping the index if it violates rules
                j -= 1 #move back one iteration and try again
                flag = False #labels current line as incorrect
                break
        j+=1
    if(not flag): #only add if line is incorrect
        ans2 += int(update[len(update)//2])
print(ans2)

