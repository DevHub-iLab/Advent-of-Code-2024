from collections import Counter
file = open("day11\day11.txt", 'r')
for line in file:
    stonesL = map(int, line.split()) #turn into list of ints, instead of strs
    stones = Counter(stonesL) #Throw list into counter

    for i in range(1, 76):
        newStones = Counter()
        for curr in stones:
            size = len(str(curr))
            if(curr == 0):
                newStones[1] += stones[curr]
            elif(size%2 == 0):
                newStones[int(str(curr)[:size//2])] += stones[curr] #First Half
                newStones[int(str(curr)[size//2:])] += stones[curr] #Second Half
            else:
                newStones[curr*2024] += stones[curr]
        stones = newStones #override

        if(i==25 or i==75):
            ans = sum([i for i in stones.values()])
            print(ans)