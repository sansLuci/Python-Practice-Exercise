# The 'try' block lets you test a block of code for errors
# The 'except' block lets you handle the error
# The 'finally' block lets you execute code, 
#       regardless of the result of the try- and except blocks

# Single exception
'''
try:
  print(x)
except:
  print("An exception occurred")
'''

# More than one exception
'''
try:
  x = 1
  print(x/0)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
'''

# we can use 'else' if no error takes place
'''
try:
    pass
except:
    pass
else:
    print("Nothing went wrong")
'''

# finally keyword
'''
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
'''

# Raising an exception
'''
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
'''
'''
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
'''