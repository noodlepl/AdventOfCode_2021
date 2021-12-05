#! /usr/local/bin/python3

with open('05.txt', 'r') as file:
    split_data = [line.strip().split('->') for line in file]
    vents = []
    # think if it could be one comprehensive list
    for item in split_data:
        flattened_item = []
        for coords in item:
            for number in coords.strip().split(','):
                flattened_item.append(int(number))
        if flattened_item[0] == flattened_item[2] or flattened_item[1] == flattened_item[3]:
            vents.append(flattened_item)

    grid = {}

    for line in vents:
        if line[0] == line[2]:
            start = min(line[1], line[3])
            stop = max(line[1], line[3]) + 1
            for coord in range(start, stop):
                key = (line[0], coord)
                if key in grid:
                    grid[key] += 1
                else:
                    grid[key] = 1
        elif line[1] == line[3]:
            start = min(line[0], line[2])
            stop = max(line[0], line[2]) + 1
            for coord in range(start, stop):
                key = (coord, line[1])
                if key in grid:
                    grid[key] += 1
                else:
                    grid[key] = 1
    res = 0
    for k,v in grid.items():
        if v >= 2:
            res += 1
    print("part 1: {}".format(res))

#part 2
with open('05.txt', 'r') as file:
    split_data = [line.strip().split('->') for line in file]
    vents = []
    # think if it could be one comprehensive list
    for item in split_data:
        flattened_item = []
        for coords in item:
            for number in coords.strip().split(','):
                flattened_item.append(int(number))
        vents.append(flattened_item)

    grid = {}
    for line in vents:
        if line[0] == line[2]:
            start = min(line[1], line[3])
            stop = max(line[1], line[3]) + 1
            for coord in range(start, stop):
                key = (line[0], coord)
                if key in grid:
                    grid[key] += 1
                else:
                    grid[key] = 1
        elif line[1] == line[3]:
            start = min(line[0], line[2])
            stop = max(line[0], line[2]) + 1
            for coord in range(start, stop):
                key = (coord, line[1])
                if key in grid:
                    grid[key] += 1
                else:
                    grid[key] = 1
        else:
            start_x = line[0]
            step_x = (line[2]-line[0])//abs(line[2]-line[0])
            stop_x = line[2] + step_x
            
            start_y = line[1]
            step_y = (line[3]-line[1])//abs(line[3]-line[1])
            stop_y = line[3] + step_y
            for x,y in zip(range(start_x, stop_x, step_x), range(start_y, stop_y, step_y)):
                key = (x, y)
                if key in grid:
                    grid[key] += 1
                else:
                    grid[key] = 1

    res = 0
    for k,v in grid.items():
        if v >= 2:
            res += 1
    print("part 2: {}".format(res))
