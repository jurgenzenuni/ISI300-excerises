#read user input
print("program started")

#define variable
message = "Hello user give me a number"
print ("Variable defined")

#lets read and remember the input
user_input = input(message)

#data type cast
user_input = int(user_input)

print("The data type for the input is:", type(user_input))

print ("User message")
print ("User, you provided the following input:",user_input)

print ("Program end")
