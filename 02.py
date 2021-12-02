#! /usr/local/bin/python3


with open('02.txt', 'r') as file:
    horizontal = 0
    depth = 0
    data = [tuple(line.split()) for line in file]
    print(data)

    for instruction in data:
        direction = instruction[0]
        value = int(instruction[1])
        if direction == "forward":
            horizontal = horizontal + value
        elif direction == "up":
            depth = depth - value
        elif direction == "down":
            depth = depth + value
        else:
            print("unknown direction")

    print(horizontal * depth)