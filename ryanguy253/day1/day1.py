import heapq
day1 = open("resources/day1.txt","r")

data = day1.read()
array = data.split("\n")

list1 = []
list2 = []

for row in array:
    i = row.split()
    list1.append(i[0])
    list2.append(i[1])

# Heapify List1 & List2
list1 = [int(i) for i in list1]
list2 = [int(i) for i in list2]

heapq.heapify(list1)
heapq.heapify(list2)
# While heap not empty, pop and add distance to total
total = 0
while(len(list1)!=0):
    temp1 = heapq.heappop(list1)
    temp2 = heapq.heappop(list2)

    total+=abs(temp1-temp2)

print(total)

# Part 2
# Convert second list to dictionary
dict = {}

for i in list2:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i]+=1

# For every element in first list, we check for corresponding element in dictionary
# , then multiply its value with the number of occurances in the dictionary

result = 0

for code in list1:
    if code in dict:
        # result += number of occurence * code
        result += dict.get(code)*code

print(result)