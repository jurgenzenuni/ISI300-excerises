#exercise 6

my_vector = [1, 2, 3, 4, 5]

def print_up_to_value(vector, value):
    i = 0
    result = []
    while i < len(vector) and vector[i] != value:
        result.append(vector[i])
        i += 1
    if vector[i]== value:
        result.append(value)
    print(result)

print_up_to_value(my_vector, 4)
