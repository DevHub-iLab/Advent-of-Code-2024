with open("input.txt", "r") as f:
    first_list = []
    second_list = []
    for line in f:
        numbers = line.split()
        if len(numbers) == 2:
            first_list.append(int(numbers[0]))
            second_list.append(int(numbers[1]))

    first_list = sorted(first_list)
    second_list = sorted(second_list)
    distance = 0
    for i in range(len(first_list)):
        distance += abs(second_list[i] - first_list[i])

    print(distance)
