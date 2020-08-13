# All classes have a function called __init__(),
#  which is always executed when the class is being initiated

# The __init__() function is called automatically 
# every time the class is being used to create a new object


# The self parameter is a reference to the current instance of the class,
#  and is used to access variables that belongs to the class.

class Person:
    def __init__(self, name, age): # constructor
       self.name = name
       self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

###########################################
####### Method creation in a class ########
###########################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

