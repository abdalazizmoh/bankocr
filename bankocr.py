#!/bin/python
import sys

DIGIT_VALUES = {
    ' _ | ||_|': 0,
    '     |  |': 1,
    ' _  _||_ ': 2,
    ' _  _| _|': 3,
    '   |_|  |': 4,
    ' _ |_  _|': 5,
    ' _ |_ |_|': 6,
    ' _   |  |': 7,
    ' _ |_||_|': 8,
    ' _ |_| _|': 9
}

try:
    path = sys.argv[1]
except IndexError as e:
    path = input('Please, Enter the file path: ')

try:
    path
except NameError:
    print('Not valid input')
else:
    with open(path, 'r+') as f:
        lines = f.read().splitlines()


for line_number, line in enumerate(lines):
    if line_number % 4 == 0:
        completeNumber = ''
        for number_start in range(0, len(line), 3):
            number_end = number_start + 3
            number = lines[line_number][number_start:number_end] + \
                lines[line_number + 1][number_start:number_end] + \
                lines[line_number + 2][number_start:number_end]
            completeNumber += str(DIGIT_VALUES.get(number))
        try:
            print(int(completeNumber))
        except :
            print("Error in data")
