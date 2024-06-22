#exercise 7

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


my_vector = [5,6,7,8,9,5,6,7,8,9]
vec_multi_print_to_number(my_vector, 7)
