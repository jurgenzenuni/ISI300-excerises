#exercise 1

my_vector = [7, 15, 22, 23, 35, 3, 1, 11, 13, 33]

for i in range (10):
    print("from 1st to last", my_vector[i])

for i in reversed(my_vector):
    print("from last to 1st", i)

i = 0
while i < len(my_vector):
    print("from 1st to last", my_vector[i])
    i += 1

i = len(my_vector) - 1
while i >= 0:
    print("From last to 1st", my_vector[i])
    i -= 1
