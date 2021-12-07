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
        print("for common pos {} we need {} fuel".format(common_pos, fuel_needed))

    print(min(fuels))