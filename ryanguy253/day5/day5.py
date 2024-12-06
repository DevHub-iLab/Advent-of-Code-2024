day5 = open("resources/day5.txt")
data = day5.read()
data = data.split("\n")
def split_data(data):
    # Find empty space to split array
    rules = []
    pages = []

    i = 0
    while data[i] != "":
        rules.append(data[i])
        i += 1

    i += 1

    while i < len(data):
        pages.append(data[i])
        i += 1

    processed_rules = []

    for rule in rules:
        temp = rule.split("|")
        temp = [int(i) for i in temp]
        processed_rules.append(temp)

    processed_pages = []

    for page in pages:
        temp = page.split(",")
        temp = [int(i) for i in temp]
        processed_pages.append(temp)

    print(processed_rules)
    print(processed_pages)
    return processed_rules, processed_pages

######################################################################################################################################
#Part 1
######################################################################################################################################

rules, pages = split_data(data)
# Algorithm, for every page in pages, check if the page has rules that affect it, if yes, then check if valid, no then continue

def isValid(rules, page_sequence, currPage, currPageIdx):
    prerequisite_pages = []

    for rule in rules:
        if currPage == rule[1]:
            # Check if page appears before the requirement in page_sequence
            prerequisite_pages.append(rule[0])

    # Try to see if all pages that must appear before current actually do so
    for i, prerequisite_page in enumerate(prerequisite_pages):
        if prerequisite_page not in page_sequence:
            continue

        # index finds the first occurrence, and since there would only be an occurrence of a page, it finds us the index
        elif prerequisite_page in page_sequence and page_sequence.index(prerequisite_page) > currPageIdx:
            return False

    return True

def checkPagesAndAddMiddle(rules,page_sequences):
    count = 0

    for page_sequence in page_sequences:
        valid = True
        for currPageIdx,currPage in enumerate(page_sequence):
            # if is Valid, find middle value and add
            if not isValid(rules,page_sequence,currPage,currPageIdx):
                valid = False
                break
        if valid:
            count += page_sequence[int(len(page_sequence) / 2)]

    print(count)

checkPagesAndAddMiddle(rules,pages)

######################################################################################################################################
#Part 2

'''
47|13
97|13
75|13
53|13
61|13
29|13
97|29
61|29
47|29
53|29
75|29
75|47
97|47
61|53
75|53
97|53
47|53
47|61
97|61
75|61
97|75

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
'''
######################################################################################################################################
# Sort According to order in rules
'''
47|13 means 47 needs to be sorted in front of 13 , ie 47 > 13

We will go through a page sequence and sort it according to the rules
'''

def findPrerequisitePages(rules,currPage,page_sequence):
    prerequisite_pages = []

    for rule in rules:
        if currPage == rule[1] and rule[0] in page_sequence:
            # Check if page appears before the requirement in page_sequence
            prerequisite_pages.append(rule[0])

    return prerequisite_pages

def findAllPrerequisitePages(rules,page_sequence):
    # Get all prerequisite pages in an array so we can look through page_sequence to find match with prerequisite_pages

    all_prerequisite_pages = []

    for page in page_sequence:
        prerequisite_pages = findPrerequisitePages(rules,page,page_sequence)
        all_prerequisite_pages.append(prerequisite_pages)

    return all_prerequisite_pages

# Prerequisite_Pages is not all_prerequisite_pages
# [[97],[],[75,97],[47,97,75],[61,75,97,47]] (all)
# [61,75,97,47]

# Finds index of the last occurance of the prerequiste page in a page sequence
# 75,97,47,61,53
# [[97],[],[75,97],[47,97,75],[61,75,97,47]]
# eg the last occurance of prerequisite pages for 53 is index 3, 61

def findLastOccuranceIndex(prerequisite_pages,page_sequence):
    max_index = -1

    for prerequisite_page in prerequisite_pages:
        if prerequisite_page in page_sequence:
            current_index = page_sequence.index(prerequisite_page)
            if current_index > max_index:
                max_index = current_index

    return max_index

def swap(i,j,arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# Sorting is done by bubble sort
def sortAccordingToRules(rules,page_sequences):
    for page_sequence in page_sequences:
        all_prerequisite_pages = findAllPrerequisitePages(rules,page_sequence)

        # 75,97,47,61,53
        # [[97],[],[75,97],[47,97,75],[61,75,97,47]]

        # 97,75,47,61,53
        # [],[97], [75, 97], [47, 97, 75], [61, 75, 97, 47]]

        # Outer loop to iterate through the list n times
        for n in range(len(page_sequence) - 1, 0, -1):
            # Initialize swapped to track if any swaps occur
            swapped = False

            # Inner loop to compare adjacent elements
            for i in range(n):
                if all_prerequisite_pages[i]:
                    lastIndex = findLastOccuranceIndex(all_prerequisite_pages[i], page_sequence)
                    if lastIndex > i:
                        swap(lastIndex, i, page_sequence)
                        swap(lastIndex, i, all_prerequisite_pages)

                        swapped = True
            # If no swaps occurred, the list is already sorted
            if not swapped:
                break

def calculateMiddleOfSortedInvalid(rules,page_sequences,sorted_page_sequences):
    count = 0

    for i, page_sequence in enumerate(page_sequences):
        valid = True
        for currPageIdx, currPage in enumerate(page_sequence):
            # if is Valid, find middle value and add
            if not isValid(rules, page_sequence, currPage, currPageIdx):
                valid = False
                break
        if not valid:
            count += sorted_page_sequences[i][int(len(sorted_page_sequences[i])/2)]


    print(f"SortedInvalid : {count}")


# 6384 too high
import copy
page_sequences = copy.deepcopy(pages)
sortAccordingToRules(rules,pages)

# Unsorted Page Sequences
print(page_sequences)

# Sorted Page Sequences
print(pages)


calculateMiddleOfSortedInvalid(rules,page_sequences,pages)






