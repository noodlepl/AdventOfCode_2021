#! /usr/local/bin/python3

import pdb

#return winning board or None
def bingo(boards):
    for board in boards:
        for line in board:
            marked_elements = 0
            for element in line:
                if element[1] == False:
                    break
                marked_elements += 1
                if marked_elements == 5:
                    return board
        for column_index in range(len(board[0])):
            marked_elements = 0
            for line in board:
                if line[column_index][1] == False:
                    break
                marked_elements += 1
                if marked_elements == 5:
                    return board
    return None

with open('04.txt', 'r') as file:
    numbers = [int(x.strip()) for x in file.readline().split(',')]
    print(numbers)
    file.readline()
    
    boards = []
    board = []

    for line in file:
        if line == '\n':
            boards.append(board)
            board = []
            continue
        board.append([[int(number), False] for number in line.split()])
    boards.append(board)

    # print(boards)

    winner = None
    last_number = -1

    # pdb.set_trace()
    for number in numbers:
        last_number = number
        for board in boards:
            for line in board:
                for element in line:
                    if number == element[0]:
                        element[1] = True
        winner = bingo(boards)
        if winner != None:
            break

    print(winner)
    false_sum = sum([num[0] for line in winner for num in line if num[1] == False])
    print(false_sum * last_number)

        