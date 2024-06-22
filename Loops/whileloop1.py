# define a list
values = [4,32,56,42,12,12,11,11,90,95,100,40,59,77,74,33]

#for loop starts
values_l = len(values)
index = 0

# while loop
while ( index < values_l ):
    print ( "We are at index", index
            ,", and the value is", values[index])
   # print (values[index])
    index = index + 1
#for loop ends



#breaking loops
values = [4,32,56,42,6,12,11,11,90,95,100,6,59,77,74,33]
for v in values:
    print("Current number is: ", v)
    if (v==6):
        print("You won!!!")
        break


#using continue
values = [4,32,56,42,6,12,11,11,90,95,100,6,59,77,74,33]

for v in values:
    remainder = v % 2
    if (remainder == 0 ):
        #if so print rest of msg and skip loop
        print("This is an even number", v)
        continue
        #this is executed everytime        
        print("This is just another number... ", v)
        #break

#online continue example
var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")
    
