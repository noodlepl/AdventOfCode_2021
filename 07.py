#! /usr/local/bin/python3

with open('07.txt', 'r') as file:
    positions = [int(x) for x in file.readline().strip().split(',')]
    print(positions)

    start = min(positions)
    stop = max(positions)+1
    fuels = []
    for common_pos in range(start, stop):
        fuel_needed = 0
        for pos in positions:
            fuel_needed += abs(pos - common_pos)
        fuels.append(fuel_needed)

    print(min(fuels))

#part 2

with open('07.txt', 'r') as file:
    positions = [int(x) for x in file.readline().strip().split(',')]
    print(positions)

    start = min(positions)
    stop = max(positions)+1
    fuels = []
    for common_pos in range(start, stop):
        fuel_needed = 0
        for pos in positions:
            dist = abs(pos-common_pos)
            fuel_needed += int((1+dist)/2*dist)
        fuels.append(fuel_needed)

    print(min(fuels))