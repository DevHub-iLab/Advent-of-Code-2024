from collections import Counter
f = open("/workspaces/Advent-of-Code-2024/emily7lim/day11/data.txt", "r")
contents = f.read().split()

def rules(contents):
    afterblink = Counter()
    for i in contents:
        repeated = int(contents[i])
        if i == "0":
            if afterblink["1"] == 0:
                afterblink += Counter("1")
                afterblink["1"] *= repeated
            else:
                afterblink["1"] += repeated
        elif len(i) % 2 == 0:
            half = int(len(i)/2)
            left,right = i[:half], i[half:]
            right = str(int(right)) #remove leading 0

            if afterblink[left] == 0:
                afterblink += Counter([left])
                afterblink[left] *= repeated
            else:
                afterblink[left] += repeated
                
            if afterblink[right] == 0:
                afterblink += Counter([right]) 
                afterblink[right] *= repeated
            else:
                afterblink[right] += repeated
        else:
            last = str(int(i)*2024)
            if afterblink[last] == 0:
                afterblink += Counter([last])
                afterblink[last] *= repeated
            else:
                afterblink[last] += repeated
    return afterblink

def totalblink(blinknum, contents):
    for i in range(blinknum):
        contents = rules(contents)
    return sum(contents.values())

# part1
print(totalblink(25, Counter(contents)))

# part2
print(totalblink(75, Counter(contents)))