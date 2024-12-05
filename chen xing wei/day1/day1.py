file = open("day1.txt", 'r')
listL = []
listR = []
sum = 0
similarity = 0
for line in file:
        x = list(line.strip().split('   '))
        listL.append(int(x[0]))
        listR.append(int(x[1]))
listL.sort()
listR.sort()
# for i in range(len(listL)):
#     sum += abs(listL[i] - listR[i])
# print(sum)

for i in range(len(listL)):
    similarity += listL[i] * listR.count(listL[i])
print(similarity)