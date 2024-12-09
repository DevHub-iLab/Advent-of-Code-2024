file = open("day9\day9.txt", 'r')
for line in file:
    diskMap = line
    disk = ""
    free = False
    cnt, ans = 0, 0
    for c in diskMap: #constructing the disk
        if(free == False):
            disk += chr(cnt) * int(c)
            free = True
            cnt += 1
        elif(free == True):
            disk += '漢' * int(c) #'漢' used to replace '.'
            free = False

    while(disk[-1] == '漢'): #removing 漢 from the right, till it reaches smth else
        disk = disk[0: -1]
    while('漢' in disk):
        freeIdx = disk.index('漢')
        disk = disk[0: freeIdx] + disk[-1] + disk[freeIdx+1: -1] #overriding with new str
        while(disk[-1] == '漢'): #removing 漢 from the right, till it reaches smth else
            disk = disk[0: -1]

    for i in range(len(disk)): #finding sum
        ans += i * ord(disk[i])
print(ans) #part 1