#exercise 3 Write a function that prints all elements whose value is an odd number

vector = [2, 4, 5, 7, 10, 11]

def odd_value_only(vector):
    for i in vector:
        if i % 2 == 1:
            print(i)

odd_value_only(vector)
