#!/bin/python
import sys
from os import path

# Map the value of each digit in three-line as one string to its number 
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

# Open a file provided or ask for the file path
def read_file_path():
    try:
        path = sys.argv[1]
    except IndexError as e:
        path = input('Please, Enter the file path: ')
    return path

# retrive the date from the file provide
def retrive_data_from_file(path):
    try:
        with open(path, 'r') as f:
            lines = f.read().splitlines()
        return lines
    except IOError:
        print('Not valid input')
        sys.exit()

# start read every 4 lines, three-line which contain the digit number
# on each line combines three char which consist of the digit number to one string
def readocr(lines):
    list_numbers = []
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
                int(completeNumber)
                list_numbers.append(completeNumber)
            except:
                list_numbers.append("Error in data")
    return list_numbers

#Print the list of outputs
def print_list_numbers(list_numbers):
    for number in list_numbers:
        print(number)

# Call the functions in main  
if __name__ == "__main__":
    path = read_file_path()
    lines = retrive_data_from_file(path)
    list_numbers = readocr(lines)
    print_list_numbers(list_numbers)