#! /usr/local/bin/python3


with open('03.txt', 'r') as file:
    data = [tuple([b for b in line if b != '\n']) for line in file]

    gamma = ['0']*len(data[0])
    epsilon = ['0']*len(data[0])
    majority_border = len(data)//2
    print(majority_border)
    

    for idx in range(len(data[0])):
        count_0 = 0
        count_1 = 0
        for binary in data:
            if binary[idx] == '0':
                count_0 = count_0+1
            else:
                count_1 = count_1+1
            
            if count_0 > majority_border:
                gamma[idx] = 0
                epsilon[idx] = 1
                break
            if count_1 > majority_border:
                gamma[idx] = 1
                epsilon[idx] = 0            
            
    gamma_dec = 0
    for idx, b in enumerate(reversed(gamma)):
        gamma_dec += b*(2**idx)

    epsilon_dec = 0
    for idx, b in enumerate(reversed(epsilon)):
        epsilon_dec += b*(2**idx)

    print(gamma_dec*epsilon_dec)
