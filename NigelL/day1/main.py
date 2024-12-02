f = open('advent1.txt','r')

leftL = []
rightL = []
for x in f:
    cS = x.split('   ')
    leftL.append(cS[0])
    aM = cS[1].replace('\n','')
    rightL.append(aM)


sL=  sorted(leftL)
sR=  sorted(rightL)

distL = [] 
ind = 0 

for ind in range(len(sL)):

    curS = 0
    for j in range(len(sL)):
        if int(sL[ind]) == int(sR[j]):
            curS += 1  

    distL.append(int(sL[ind]) * curS)



testN = sum(distL)

print(testN)
