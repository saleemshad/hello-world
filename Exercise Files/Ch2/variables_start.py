# 
# Example file for variables
#

# Declare a variable and initialize it
f= 0
#print(f) #commented for executing function


# re-declaring the variable works

#f = "abc" #commented for executing function
#print(f) #commented for executing function

# ERROR: variables of different types cannot be combined
# to fix this convert interger to string with str() function
#print("this is the string" + str(123))


# Global vs. local variables in functions
def someFunction():
    global f # we are making local variable global by declaring this
    f="def"
    print(f)

someFunction()
print(f)

del f
print(f)
