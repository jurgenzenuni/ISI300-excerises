#Exercise 8

my_vector = [1,2,3,4,5,6,7,8,9,10]

i = 0
odd_numbers = []
even_numbers = []

while i < len(my_vector):
    if my_vector[i] % 2 == 1:
        odd_numbers.append(my_vector[i])
    else:
        even_numbers.append(my_vector[i])
    i += 1

print(odd_numbers, even_numbers)
