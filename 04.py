#! /usr/local/bin/python3

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

def is_bingo(board):
    for line in board:
        marked_elements = 0
        for element in line:
            if element[1] == False:
                break
            marked_elements += 1
            if marked_elements == 5:
                return True
    for column_index in range(len(board[0])):
            marked_elements = 0
            for line in board:
                if line[column_index][1] == False:
                    break
                marked_elements += 1
                if marked_elements == 5:
                    return True
    return False
                

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

    winner = None
    last_number = -1

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
    false_sum = sum([num[0] for line in winner for num in line if num[1] == False])
    print(false_sum)
    print(last_number)
    print(false_sum * last_number)

    # part 2
    for number in numbers:
        last_number = number
        for board in boards:
            for line in board:
                for element in line:
                    if number == element[0]:
                        element[1] = True
        if len(boards) > 1:
            boards = [b for b in boards if not is_bingo(b)]
        else:
            if is_bingo(boards[0]):
                winner = boards[0]
                break

    print(boards)
    false_sum = sum([num[0] for line in winner for num in line if num[1] == False])
    print(false_sum)
    print(last_number)
    print(false_sum * last_number)

        