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