#define an array
values = [5,10,15,20,25]

#Function for printing sequence of numbers
def print_seq(seq):
    for v in values:
        print ("Value:", v)
print_seq(values)

#function for sum
def sum_values(seq):
    total = 0
    for v in values:
        total = total + v
    return total
print("The grand total is: ", sum_values(values))

