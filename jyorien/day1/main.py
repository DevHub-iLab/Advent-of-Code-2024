list1 = []
list2 = []
with open("day1.txt", "r") as file:
    for line in file:
        l, r = line.split("   ")
        list1.append(int(l))
        list2.append(int(r))
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)
difference = []
for i in range(len(sorted_list1)):
    diff = abs(sorted_list1[i] - sorted_list2[i])
    difference.append(diff)

print(sum(difference))

freq = {}
for ele in list2:
    if ele not in freq:
        freq[ele] = 1
    else:
        freq[ele] += 1

sum = 0
for ele in list1:
    if ele in freq:
        sum += ele * freq[ele]

print(sum)


