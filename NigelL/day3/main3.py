import re

f = open('advent3.txt','r')
mF = f.read()
x = re.findall("mul\([0-9]+,[0-9]+\)", mF)

#First star

res = 0

for i in range(len(x)):         
    gC = re.findall(r'\d+',x[i])
    res += int(gC[0]) * int(gC[1])


print(res)

#Second star
allI = [(m.start(0), m.end(0)) for m in re.finditer("mul\([0-9]+,[0-9]+\)",mF )]

allDo = [(m.start(0), m.end(0)) for m in re.finditer("do\(\)",mF )]
allDont = [(m.start(0), m.end(0)) for m in re.finditer("don't\(\)",mF )]

res = 0  
doMul = True

do_index = 0 
dont_index = 0

for i in range(len(x)):
    cIndex = allI[i][0]
    while (cIndex > allDont[dont_index][0] or cIndex > allDo[do_index][0]):
        if (cIndex > allDont[dont_index][0]):
            doMul  = False
            if dont_index < len(allDont) - 1:
                 dont_index +=1
        if cIndex > allDo[do_index][0]:
            doMul = True
            if do_index < len(allDo) - 1:
                 do_index +=1
        
        if do_index == len(allDo) - 1 and dont_index == len(allDont) - 1:
            break
         
    if doMul:
        gC = re.findall(r'\d+',x[i])
        res += int(gC[0]) * int(gC[1])
    

print(res)
