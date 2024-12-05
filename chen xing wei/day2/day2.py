total = 0
with open("day2.txt", "r") as file:
    for line in file:
        strs = line.split(" ")
        ints = [int(i) for i in strs]

        direction = 0
        for i in range(len(ints)-1):
            if(abs(ints[i]-ints[i+1]) > 3 or abs(ints[i]-ints[i+1]) == 0):
                break
            if(direction==0):
                if(ints[i]>ints[i+1]):
                    direction = -1
                elif(ints[i]<ints[i+1]):
                    direction = 1
            else:
                if(direction==1 and ints[i]>ints[i+1]):
                    break
                elif(direction==-1 and ints[i]<ints[i+1]):
                    break
            if(i == len(ints)-2):
                total += 1
print(total)