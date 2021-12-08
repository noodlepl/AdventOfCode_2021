#! /usr/local/bin/python3

with open('08.txt', 'r') as file:
    digits = [[d for d in line.strip().split('|')[1].split()] for line in file]
    print(digits)

    count_unique = 0
    unique_lengths = [2, 3, 4, 7]
    for number in digits:
        for digit in number:
            if len(digit) in unique_lengths:
                count_unique += 1
    print(count_unique)