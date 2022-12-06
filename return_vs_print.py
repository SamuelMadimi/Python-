# -*- coding: utf-8 -*-
"""return-vs-print.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/SamuelMadimi/1d2fa16f7d0671999c2590c82feaff4a/return-vs-print.ipynb
"""

# This is defining Definition:

def add(x,y):
  print (x+y)

# THis is how we call the defined definition -> Argument

add(5,7)   # Output = 12

# This is defining Definition:

def add(x,y):
  return (x+y)

# THis is how we call the defined definition -> Argument
add(5,7)   # Output = 12

"""In both the above pieces, the output is same. But look at the below pieces for the fiffernce between 'return' and 'print'"""

def add(x, y):
    return (x + y)

result = add(2, 3)

print(result)
# based on the arguments, the code returns a value and this is not visible. since we desined a varioable 'result' , the result value is stored in the variable  so that, I can
# use the returned value in my code in my program anywhere. 

# I can even print the variable to see the returned value.

def add(x, y):
    print (x + y) # Gives out value ' 5 '


result = add(2, 3)  # But here, we are callinhg the function which do not have 'return statement' Since the functions return nothing, printing it gives out 'None'
                    # Therefore, 'None' is the value assigned to the variable 'result' The below statement prints 'None'

print(result)   # This statment is the reason for 'None'

# When we call a python function that doesn't have a 'return' statement, the value returned will be 'None'.

def add(x, y):
    print (x + y) # Gives out value ' 5 '
  
add(2,3) # here we are calling the function directly (or using in a program) and printing the value. But not assigning the value to a variable.