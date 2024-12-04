import re
with open("input.txt") as file:
    text = file.read()
    sum = 0
    muls = re.findall(r"mul\(\d+\.?\d*,\d+\.?\d*\)", text)
    for mul in muls:
        firstPart, secondPart = mul.split(",")
        firstPart = int(firstPart.split("(")[1])
        secondPart = int(secondPart.split(")")[0])
        sum += firstPart * secondPart
    print(sum)

    sum2 = 0
    mulsWithConditions = re.findall(r"mul\(\d+\.?\d*,\d+\.?\d*\)|\bdon't\(\)|\bdo\(\)", text)
    lastCondition = True
    for ele in mulsWithConditions:
        if ele == "don't()":
            lastCondition = False
        elif ele == "do()":
            lastCondition = True
        else:
            if lastCondition:
                firstPart, secondPart = ele.split(",")
                firstPart = int(firstPart.split("(")[1])
                secondPart = int(secondPart.split(")")[0])
                sum2 += firstPart * secondPart
    print(sum2)
