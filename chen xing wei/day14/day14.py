file = open("day14\day14.txt", 'r')
q1, q2, q3, q4, ans2 = 0,0,0,0,0
halfW, halfH = 101//2, 103//2
Positions, Velocities = [], []
for i in file:
    line = i.strip().split(" ")
    pos = line[0].split(",")
    posX, posY = int(pos[0][2:]), int(pos[1]) 
    vel = line[1].split(",")
    velX, velY = int(vel[0][2:]), int(vel[1])
    Positions.append([posX, posY]) #append for part 2
    Velocities.append([velX, velY])
    posX, posY = (posX+velX*100)%101, (posY+velY*100)%103 #Find pos after 100secs

    if(posX<halfW and posY<halfH):
        q1+=1
    elif(posX>halfW and posY<halfH):
        q2+=1
    elif(posX<halfW and posY>halfH):
        q3+=1
    elif(posX>halfW and posY>halfH):
        q4+=1

#Part 2 the easter egg is that we have to find a time when all robots occupy an unique pos
christmasTree = False
seconds = 0
while(not christmasTree):
    seconds += 1
    loopPos = []
    for i in range(len(Positions)):
        #Calculate the curr pos for this robot at this time
        currPos = [(Positions[i][0]+Velocities[i][0]*seconds)%101, (Positions[i][1]+Velocities[i][1]*seconds)%103]
        #If there is an instance of another robot at this pos on this time it goes to the next second
        if(currPos in loopPos):
            break
        loopPos.append(currPos)

        if(i==len(Positions)-1): #Found Tree
            christmasTree = True
            for y in range(103):
                for x in range(101):
                    if([x,y] in loopPos):
                        print('X', end='')
                    else:
                        print('.', end='')
                print()

print("Part 1:", q1*q2*q3*q4, "\nPart 2:", seconds)