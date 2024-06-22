#read input
user_input = input("please enter an integer: ")

#convert input to number
a = int(user_input)

#evaluate
if (a > 0 ):
    print("Positive")
elif (a < 0):
    print("Negative")
else: print("Neutral")
