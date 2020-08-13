'''
class Person: # Parent class or Base class or Super class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)

class Student(Person): # Clild class or Sub class
    pass

x = Student("Mike", "Malen")
x.print_name()
'''

# When you add the __init__() function to the child, 
# the child class will no longer inherit the parent's __init__() function
# so we need to call parent's __init__() function
'''
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
'''
# We can use super() method instead of writing the name of parent class
'''
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
'''
# We can add methods and parameters in the subclass
'''
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
'''