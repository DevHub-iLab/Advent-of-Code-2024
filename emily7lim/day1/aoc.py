##path in codespace
f = open("/workspaces/Advent-of-Code-2024/emily7lim/day1/data.txt", "r")
contents = f.read().split()
left = []
right = []
distsum = []
for i in range(len(contents)):
    if i%2==0:
        right.append(int(contents[i]))
    else:
        left.append(int(contents[i]))

#part1
left.sort()
right.sort()
for i in range(len(left)):
    distsum.append(abs(left[i]-right[i]))
print(sum(distsum))

# part2
ss = 0
for i in left:
    if i in right:
        ss += right.count(i)*i
    else:
        ss += 0

print(ss)