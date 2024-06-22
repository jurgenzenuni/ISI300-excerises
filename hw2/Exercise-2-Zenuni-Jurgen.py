#exercise 2

vector = [7, 15, 10, 2, 55, 4]

def odd_index_only(vector):
    for i in range(len(vector)):
        if i % 2 == 1:
            print(vector[i])
            
odd_index_only(vector)
