f = open('advent2.txt','r')

safeC = 0

for x in f:
    aS = x.split(' ') 
    sOp = 0 
    sOrNot = 0
    for i in range(len(aS) - 1): 
        cR = int(aS[i]) - int(aS[i + 1])
        if abs(cR) > 3 or abs(cR) < 1:
            sOrNot += 1
            if (sOrNot >= 2 ):
                break
                 
        if sOp != 0:
            if cR > 0 and sOp < 0:
                sOrNot += 1
                if (sOrNot >= 2 ):
                    break
                     
            elif cR < 0 and sOp > 0:
                sOrNot += 1
                if (sOrNot >= 2 ):
                    break
        else:
            if cR > 0: 
                sOp = 1
            else:
                sOp = -1

    if sOrNot <= 1:
        safeC += 1 

print(safeC)

