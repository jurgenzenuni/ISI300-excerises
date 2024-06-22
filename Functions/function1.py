





#define list
values_1 = [2023,2,6,11,7,8]
values_2 = [4456,56,77,2,1,78]

#function to calc sum of the numbers
def sum_all_nums(a_list):
    running_sum = 0
    for a_value in a_list:
        runnning_sum = running_sum + a_value
        print("Running sum:", running_sum)

    print("Total:", running_sum)

sum_all_nums(values_1)



# define a list
values_1 = [2023,2,6,11,7,8]
values_2 = [4456,72,3,1,4,72,72,54]

def sum_all_numbers(a_list):
    running_sum = 0
    for a_value in a_list:
        running_sum = running_sum + a_value
        print("Running sum:",running_sum)

    print("Total:",running_sum)

sum_all_numbers(values_1)
sum_all_numbers(values_2)


# define a list
values_1 = [2023,2,6,11,7,8]
values_2 = [4456,72,3,1,4,72,72,54]

def sum_all_numbers(a_list):
    running_sum = 0
    for a_value in a_list:
        running_sum = running_sum + a_value

        return running_sum

sum_of_list_1 = sum_all_numbers(values_1)
print("The list has sum")
sum_all_numbers(values_1)
sum_all_numbers(values_2)
