# Lambda Function

# lambda var: logic
# double = lambda a : a * n
# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

def func(n):
      return lambda a : a * n

double = func(2) # value of n

print(double(11)) # value of a

# def myfunc(n):
#       return n

# double = myfunc(2)
# print(double)