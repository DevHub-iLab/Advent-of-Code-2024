import aocd
input = aocd.get_data(year=2024, day=9)
# input = """2333133121414131402"""
input = [int(x) for x in input]

### Part 1
def generate_diskspace(diskmap):
    out = []
    for i in range(len(diskmap)):
        if i % 2 == 0:
            for _ in range(int(diskmap[i])):
                out.append(str(i // 2))
        else:
            for _ in range(int(diskmap[i])):
                out.append('.')

    return out
# print(generate_diskspace(input))

# Move last non '.' to the first '.'
def move_blocks(diskspace):
    front = 0
    back = len(diskspace) - 1
    while front < back:
        if diskspace[front] == '.':
            while diskspace[back] == '.':
                back -= 1
            diskspace[front], diskspace[back] = diskspace[back], diskspace[front]
        front += 1
    return diskspace

# print("".join(move_blocks(generate_diskspace(input))))

def checksum(diskspace):
    sum = 0
    for i in range(len(diskspace) - 1):
        if diskspace[i] != '.':
            sum += i * int(diskspace[i])

    return sum

print(checksum(move_blocks(generate_diskspace(input))))

### Part 2. We opt for the slow naive solution
# Ideally, we should keep a hashmap of the available run lengths of '.'s to make it more efficient
# However, I'm sleep deprived so screw it

# first index of that has a runLength runlength of '.'s
def find_first(runLength, diskspace, before):
    for i in range(len(diskspace) - runLength + 1):
        correct = True
        for j in range(runLength):
            if diskspace[i + j] != '.':
                correct = False
                break
        if correct:
            if i < before:
                return i
            else:
                return -1
    return -1

def move_block_groups(diskspace):
    back = len(diskspace) - 1
    while back >= 0:
        # Find the first non '.' entry from the back
        while diskspace[back] == '.':
            back -= 1
        grpLength = 0

        while diskspace[back] == diskspace[back - grpLength]:
            grpLength += 1
        index =  find_first(grpLength, diskspace, back)
        if index == -1:
            back -= grpLength
        else:
            for i in range(grpLength):
                diskspace[index + i], diskspace[back - i] = diskspace[back - i], diskspace[index + i]    
        
    return diskspace

print(checksum(move_block_groups(generate_diskspace(input))))