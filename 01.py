#! /usr/local/bin/python3

with open('01.txt', 'r') as file:
    data = [int(line) for line in file]
    
    res = 0
    prev = data[0]
    for x in data[1:]:
        if x > prev:
            res = res+1
        prev = x

    print(res)

    #part 2

with open ('01.txt', 'r') as file:
    data = [int(line) for line in file]

    res = 0

    prev = sum(data[0:3])
    for idx, value in enumerate(data[1:-2], start=1):
        current = data[idx] + data[idx+1] + data[idx+2]
        if (current > prev):
            res = res + 1
        prev = current
    print(res)