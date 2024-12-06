# Data Preparation
import numpy as np

day4 = open("resources/day4.txt")
data = day4.read()
data = data.split("\n")
word_search_array = []

for i in data:
    temp = list(i)
    word_search_array.extend([temp])

print(np.matrix(word_search_array))

num_rows = 0
num_cols = 0
###############################################################################################################################################
# Part 1
###############################################################################################################################################
# Finding Match
def isValid(i, j):
    return 0 <= i < num_rows and 0 <= j < num_cols


# Recursive Implementation to solve
def try_to_find_match(i, j, dx, dy, word, word_idx, count):
    global word_search_array

    # Base Case, end recursion when word is at last index
    if word_idx == len(word) - 1:
        if word_search_array[i][j] == word[word_idx]:
            count[0] += 1
        return

    if word_search_array[i][j] == word[word_idx]:
        if isValid(i+dx,j+dy) and word_search_array[i+dx][j+dy] == word[word_idx+1]:
            try_to_find_match(i+dx, j+dy, dx,dy,word, word_idx + 1, count)

def count_word_occurances(word_search_array, word):
    global num_cols
    global num_rows

    num_rows = len(word_search_array)
    num_cols = len(word_search_array[0])

    count = [0]

    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1))

    for i in range(num_rows):
        for j in range(num_cols):

            # We want the solution to take only 1 direction, or else it would count
            #   S
            # XMA        as a solution, which is wrong, so we keep track of the dir

            for dx, dy in dirs:
                try_to_find_match(i,j, dx, dy, word, 0, count)

    return count

print(count_word_occurances(word_search_array, "XMAS"))

###############################################################################################################################################
# Part 2
###############################################################################################################################################

# Check for all patterns of X-MAS cross
# Approach : Look through the matrix, and find an A, then we check the upper and lower diagonals for the letter M and S
'''
M       S
    A
M       S
'''

def checkXmasCross(i,j):
    if isValid(i-1,j-1) and isValid(i-1,j-1) and isValid(i+1,j-1) and isValid(i+1,j+1) and word_search_array[i][j] == "A":
        down_diagonal_has_MAS = (word_search_array[i-1][j-1] == "M" and word_search_array[i+1][j+1] == "S") or (word_search_array[i-1][j-1] == "S" and word_search_array[i+1][j+1] == "M")
        up_diagonal_has_MAS = (word_search_array[i+1][j-1] == "M" and word_search_array[i-1][j+1] == "S") or (word_search_array[i+1][j-1] == "S" and word_search_array[i-1][j+1] == "M")
        return down_diagonal_has_MAS and up_diagonal_has_MAS

def countXmasCross(word_search_array):
    global num_cols
    global num_rows

    num_rows = len(word_search_array)
    num_cols = len(word_search_array[0])

    count = 0

    for i in range(num_rows):
        for j in range(num_cols):
            if checkXmasCross(i,j):
                count += 1

    print(count)

countXmasCross(word_search_array)



