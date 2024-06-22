#exercise 5

my_vector = [1, 2, 3, 4, 5]

def swap(my_vector, i, x):
    my_vector[i], my_vector[x] = my_vector[x], my_vector[i]
    print(my_vector)

swap(my_vector,0 ,1)
