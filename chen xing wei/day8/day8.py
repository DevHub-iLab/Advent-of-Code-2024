file = open("day8\day8.txt", 'r')
freq = {}
y = 0
for i in file:
    line = list(i.strip())
    for x in range(len(line)):
        if(line[x] != "."):
            if line[x] in freq:
                freq[line[x]].append([y, x])
            else:
                freq[line[x]] = [[y, x]]
    y += 1

ans1, ans2 = 0, 0
nodeLoc = []
for key, value in freq.items():
    freqIns = len(value)
    for i in range(freqIns):
        for j in range(i+1, freqIns):
            distY = value[i][0] - value[j][0]
            distX = value[i][1] - value[j][1]
            if(value[i][0]+distY>=0 and value[i][1]+distX>=0 and value[i][1]+distX<50):
                if([value[i][0]+distY, value[i][1]+distX] not in nodeLoc):
                    nodeLoc.append([value[i][0]+distY, value[i][1]+distX])
                    ans1 += 1
            if(value[j][0]-distY<y and value[j][1]-distX>=0 and value[j][1]-distX<50):
                if([value[j][0]-distY, value[j][1]-distX] not in nodeLoc):
                    nodeLoc.append([value[j][0]-distY, value[j][1]-distX])
                    ans1 += 1


nodeLoc = []
for key, value in freq.items():
    freqIns = len(value)
    for i in range(freqIns):
        for j in range(i+1, freqIns):
            distY = value[i][0] - value[j][0]
            distX = value[i][1] - value[j][1]
            mul = 0
            #same thing as part1 just that now it is more strict with the x coor, and there is a multiplier for dists
            if(distX >= 0):
                while(value[i][0]+distY*mul>=0 and value[i][1]+distX*mul<50):
                    if([value[i][0]+distY*mul, value[i][1]+distX*mul] not in nodeLoc):
                        nodeLoc.append([value[i][0]+distY*mul, value[i][1]+distX*mul])
                        ans2 += 1
                    mul+=1
                mul = 0
                while(value[j][0]-distY*mul<y and value[j][1]-distX*mul>=0):
                    if([value[j][0]-distY*mul, value[j][1]-distX*mul] not in nodeLoc):
                        nodeLoc.append([value[j][0]-distY*mul, value[j][1]-distX*mul])
                        ans2 += 1
                    mul+=1
            else:
                while(value[i][0]+distY*mul>=0 and value[i][1]+distX*mul>=0):
                    if([value[i][0]+distY*mul, value[i][1]+distX*mul] not in nodeLoc):
                        nodeLoc.append([value[i][0]+distY*mul, value[i][1]+distX*mul])
                        ans2 += 1
                    mul+=1
                mul = 0
                while(value[j][0]-distY*mul<y and value[j][1]-distX*mul<50):
                    if([value[j][0]-distY*mul, value[j][1]-distX*mul] not in nodeLoc):
                        nodeLoc.append([value[j][0]-distY*mul, value[j][1]-distX*mul])
                        ans2 += 1
                    mul+=1
print("1:", ans1, "\n2:", ans2)