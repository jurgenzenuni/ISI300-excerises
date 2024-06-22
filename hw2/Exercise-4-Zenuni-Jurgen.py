#exercise 4

my_vector = [1, 2, 3, 4, 5]

def vector_sum(my_vector):
    print(sum(my_vector))

def vector_prod(my_vector):
    prod = 1
    for i in my_vector:
        prod *= i
    print(prod)

def vector_max(my_vector):
    print(max(my_vector))

def vector_min(my_vector):
    print(min(my_vector))


print("my_vector", my_vector)
print("Returns the sum of all elements")
vector_sum(my_vector)
print("Returns the prod of all elements")
vector_prod(my_vector)
print("Returns the max of all elements")
vector_max(my_vector)
print("Returns the min of all elements")
vector_min(my_vector)
