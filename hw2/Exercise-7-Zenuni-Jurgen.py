#exercise 7

my_vector = [1,2,3,4,5,3,2,4,5,3]

def vec_multi_print_to_number(vector, value):
    i = 0
    count = 0
    result = []
    while i < len(vector) and count < 2:
        result.append(vector[i])
        if vector[i] == value:
            count += 1
        i += 1
    print(result)


vec_multi_print_to_number(my_vector, 4)
