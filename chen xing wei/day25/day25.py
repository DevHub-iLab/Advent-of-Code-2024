file = open("day25\day25.txt", "r")
data = file.read()
bruh = data.split("\n\n")
locks, keys = [], []

def thing(what): #fn used to count. param is lock or key
    curr = [0, 0, 0, 0, 0]
    for row in i.split('\n')[1:-1]: #skip first and last row of block
        for x, col in enumerate(row):
            if(col == '#'):
                curr[x] += 1
        if(curr not in what):
            what.append(curr)

for i in bruh:
    if(i[0]=='#'): #lock
        thing(locks)
    else: #keys
        thing(keys)

ans = 0
for key in keys:
    for lock in locks:
        fit = True
        for i in range(5):
            if(key[i]+lock[i] > 5): #if adding up is more than 5 it dun fit
                fit = False
                break
        if(fit): 
            ans += 1
print(ans)