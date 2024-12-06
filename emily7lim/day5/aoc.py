import functools

f = open("/workspaces/Advent-of-Code-2024/emily7lim/day5/data.txt", "r")
contents = f.read().split("\n\n")
        
pagelist = []
for i in contents[0].split("\n"):
    page = i.split("|")
    pagelist.append(page)

requirements = {}
for value,key in pagelist:
    if key not in requirements.keys():
        requirements[key] = [value]
    elif value not in requirements.values():
        requirements[key].append(value)

allpage = [i.split(",") for i in contents[1].split("\n")]

def paging(x,y):
    if x==y:
        return 0
    if x in requirements:
        if y in requirements[x]:
            return 1
    if y in requirements:
        if x in requirements[y]:
            return -1
    return 0

middle = 0
wrong = []
for i in allpage:
    #part1
    if i == sorted(i, key = functools.cmp_to_key(paging)):
        middle += int(i[len(i)//2])
    else:
        #part2
        wrong.append(i)
print(middle)

mwrong = 0
for i in wrong:
    sortedi = sorted(i, key = functools.cmp_to_key(paging))
    mwrong += int(sortedi[len(sortedi)//2])

print(mwrong)