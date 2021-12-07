#! /usr/local/bin/python3

with open('06.txt', 'r') as file:
    lanternfish = [int(num) for num in file.readline().strip().split(',')]

    for day in range(80):
        print(day)
        fish_to_add = 0
        for idx, fish in enumerate(lanternfish):
            if fish == 0:
                lanternfish[idx] = 6
                fish_to_add += 1
                continue
            lanternfish[idx] -= 1
        lanternfish.extend([8]*fish_to_add)
    
    print(len(lanternfish))

    #part 2
    fish_dict = {}
    for num in range(9):
        count_num = lanternfish.count(num)
        fish_dict[num] = count_num

    print(fish_dict)
    for day in range(256):
        zeros_temp = fish_dict[0]
        for fish in range(8):
            fish_dict[fish] = fish_dict[fish+1]
        fish_dict[8] = zeros_temp
        fish_dict[6] += zeros_temp
    
    print(fish_dict)
    sum = 0
    for k,v in fish_dict.items():
        sum += v
    print(sum)