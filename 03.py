#! /usr/local/bin/python3

def convert_binary(binary):
    res = 0
    for idx, b in enumerate(reversed(binary)):
        res += int(b)*(2**idx)
    return res

with open('03.txt', 'r') as file:
    data = [tuple([b for b in line if b != '\n']) for line in file]

    gamma = ['0']*len(data[0])
    epsilon = ['0']*len(data[0])
    majority_border = len(data)//2
    
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
            
    gamma_dec = convert_binary(gamma)
    epsilon_dec = convert_binary(epsilon)

    print(gamma_dec*epsilon_dec)

# part 2

def find_number(data, idx, majority=True):
    if len(data) == 1:
        print('{} found at idx {}'.format(data, idx))
        return data[0]

    count_0 = 0
    count_1 = 0
    majority_border = len(data)//2
    org = []
    for binary in data:
        if binary[idx] == '0':
            count_0 = count_0+1
        else:
            count_1 = count_1+1
        if count_0 > majority_border:
            org = [line for line in data if line[idx] == ('0' if majority else '1')]
            break
        if count_1 > majority_border:
            org = [line for line in data if line[idx] == ('1' if majority else '0')]
            break
    if count_0 == majority_border and count_0 == count_1:
        org = [line for line in data if line[idx] == ('1' if majority else '0')]
    return find_number(org, idx+1, majority)
        

with open('03.txt', 'r') as file:
    data = [tuple([b for b in line if b != '\n']) for line in file]

    org = convert_binary(find_number(data, 0))
    csr = convert_binary(find_number(data, 0, False))

    print('org={} csr={} res={}'.format(org, csr, org*csr))
    