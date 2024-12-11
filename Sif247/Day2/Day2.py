with open("input.txt", "r") as f:
    ris = 0
    for line in f:
        levels = list(map(int, line.split()))

        diff = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
        if all(1 <= i <= 3 for i in diff):
            ris += 1
        elif all(-3 <= i <= -1 for i in diff):
            ris += 1

    print(ris)
