def num_to_digit(num : str)->list[int]:
    num_list = []
    num_int = int(num)

    for i in range(len(num),0,-1):
        result = num_int//(10**(i-1))
        num_int = num_int%(10**(i-1))
        num_list.append(result)
    return num_list

